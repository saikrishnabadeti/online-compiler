##################################################################
################ This language by Rahul ##########################
##################################################################



# app/routers/compiler_languages.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
from typing import List, Dict, Any
 
from pydantic import BaseModel
 
from app.db import get_db
from ..schemas.language import (
    LanguageCreate, LanguageUpdate,
    LanguageOut, LanguagesBulkCreate
)
from app.models.compiler import LanguagesInfo
 
router = APIRouter(prefix="/languages", tags=["Languages"])
 
 
# Response model for bulk create result
class BulkCreateResult(BaseModel):
    added: List[LanguageOut]
    skipped: List[Dict[str, Any]]  # each entry: {"lang_name": str, "reason": str}
 
 
# ---------------------------------------------
# CREATE ONE LANGUAGE (case-insensitive, trimmed)
# ---------------------------------------------
@router.post("/", response_model=LanguageOut)
def create_language(data: LanguageCreate, db: Session = Depends(get_db)):
    name = (data.lang_name or "").strip()
    if not name:
        raise HTTPException(status_code=400, detail="lang_name is required")
 
    # case-insensitive check
    exists = db.query(LanguagesInfo).filter(
        func.lower(LanguagesInfo.lang_name) == name.lower()
    ).first()
    if exists:
        raise HTTPException(status_code=400, detail="Language already exists")
 
    new_lang = LanguagesInfo(lang_name=name, description=data.description)
    try:
        db.add(new_lang)
        db.commit()
        db.refresh(new_lang)
    except IntegrityError:
        db.rollback()
        # handle rare race condition where another process inserted same name
        raise HTTPException(status_code=400, detail="Language already exists (race)")
 
    return new_lang
 
 
# ---------------------------------------------
# BULK CREATE LANGUAGES (case-insensitive, avoids duplicates + race-safe)
# ---------------------------------------------
@router.post("/bulk", response_model=BulkCreateResult)
def bulk_create_languages(payload: LanguagesBulkCreate, db: Session = Depends(get_db)):
    added_models: List[LanguagesInfo] = []
    skipped: List[dict] = []
 
    # track normalized names seen in this request to avoid duplicates in same payload
    seen_normalized = set()
 
    for item in payload.languages:
        raw_name = (item.lang_name or "")
        name = raw_name.strip()
        if not name:
            skipped.append({"lang_name": raw_name, "reason": "Empty or invalid name"})
            continue
 
        normalized = name.lower()
        # avoid duplicate entries within same payload (case-insensitive)
        if normalized in seen_normalized:
            skipped.append({"lang_name": name, "reason": "Duplicate in request payload"})
            continue
        seen_normalized.add(normalized)
 
        # Case-insensitive DB check
        existing = db.query(LanguagesInfo).filter(
            func.lower(LanguagesInfo.lang_name) == normalized
        ).first()
        if existing:
            skipped.append({"lang_name": name, "reason": "Language already exists"})
            continue
 
        # Try to insert and commit per item to detect race insert by other processes
        lang = LanguagesInfo(lang_name=name, description=item.description)
        db.add(lang)
        try:
            db.commit()
            db.refresh(lang)
            added_models.append(lang)
        except IntegrityError:
            db.rollback()
            skipped.append({"lang_name": name, "reason": "Language already exists (race)"})
 
    return BulkCreateResult(added=added_models, skipped=skipped)
 
 
# ---------------------------------------------
# GET ALL LANGUAGES
# ---------------------------------------------
@router.get("/", response_model=List[LanguageOut])
def get_languages(db: Session = Depends(get_db)):
    return db.query(LanguagesInfo).all()
 
 
# ---------------------------------------------
# GET SINGLE LANGUAGE
# ---------------------------------------------
@router.get("/{lang_id}", response_model=LanguageOut)
def get_language(lang_id: int, db: Session = Depends(get_db)):
    lang = db.query(LanguagesInfo).filter(LanguagesInfo.lang_id == lang_id).first()
    if not lang:
        raise HTTPException(status_code=404, detail="Language not found")
    return lang
 
 
# ---------------------------------------------
# UPDATE LANGUAGE (case-insensitive uniqueness enforced)
# ---------------------------------------------
@router.put("/{lang_id}", response_model=LanguageOut)
def update_language(lang_id: int, data: LanguageUpdate, db: Session = Depends(get_db)):
    lang = db.query(LanguagesInfo).filter(LanguagesInfo.lang_id == lang_id).first()
    if not lang:
        raise HTTPException(status_code=404, detail="Language not found")
 
    if data.lang_name is not None:
        new_name = data.lang_name.strip()
        if not new_name:
            raise HTTPException(status_code=400, detail="lang_name cannot be empty")
 
        # check for other row with same name (case-insensitive)
        conflict = db.query(LanguagesInfo).filter(
            func.lower(LanguagesInfo.lang_name) == new_name.lower(),
            LanguagesInfo.lang_id != lang_id
        ).first()
        if conflict:
            raise HTTPException(status_code=400, detail="Another language with same name exists")
 
        lang.lang_name = new_name
 
    if data.description is not None:
        lang.description = data.description
 
    try:
        db.commit()
        db.refresh(lang)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Could not update language (integrity error)")
 
    return lang
 
 
# ---------------------------------------------
# DELETE LANGUAGE
# ---------------------------------------------
@router.delete("/{lang_id}")
def delete_language(lang_id: int, db: Session = Depends(get_db)):
    lang = db.query(LanguagesInfo).filter(LanguagesInfo.lang_id == lang_id).first()
    if not lang:
        raise HTTPException(status_code=404, detail="Language not found")
 
    db.delete(lang)
    db.commit()
    return {"message": "Language deleted successfully"}
