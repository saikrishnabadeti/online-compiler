from fastapi import APIRouter, HTTPException, Body, Depends, Query, status, UploadFile
from typing import Annotated
from sqlalchemy.orm import Session
import pandas as pd
from io import StringIO
import json
from fastapi.encoders import jsonable_encoder
from pydantic import ValidationError


from ..schemas.compiler_question import AddQuestion, QuestionBase, UpdateQuestion, QuestionTestCase, QuestionResponse
from ..db import get_db
from ..models.compiler import Questions


router = APIRouter(prefix="/compiler-questions", tags=["Compiler-Questions"])


@router.post("/add", response_model=QuestionResponse)
async def add_single_question(
    request_body:Annotated[AddQuestion, Body()],
    db:Annotated[Session, Depends(get_db)],
):
    try:
        ## check is dupilicate question is trying to add
        ## ----------------------------------------------
        if db.query(Questions).filter(
            Questions.title == request_body.title,
            ).first():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Question alredy existed"
            )
        ## ----------------------------------------------



        data = Questions(**request_body.model_dump())
        db.add(data)
        db.commit()
        return data
    except Exception as e:
        raise e

@router.post("/upload-csv")
async def add_multiple_question(
    file:UploadFile,
    db:Annotated[Session, Depends(get_db)],

):
    try:
        if not file.filename.endswith('.csv'):
            raise HTTPException(status_code=400, detail="File must be a CSV")
        
        # Read the uploaded CSV file
        content = await file.read()
        df = pd.read_csv(StringIO(content.decode('utf-8')))

        # Validate expected columns
        expected_columns = ['title', 'question', 'description', 'sample_inputs', 'sample_outputs', 'test_cases']
        if not all(col in df.columns for col in expected_columns):
            raise HTTPException(status_code=400, detail="CSV must contain all required columns")
        
        added_q_count = 0
        for _, row in df.iterrows():

            ## check is dupilicate question is trying to add
            ## ----------------------------------------------
            if db.query(Questions).filter(
                Questions.title == row['title']
                ).first():
                continue ## countiune on next iters
            ## ----------------------------------------------   

            ## add quetion to db table
            problem = Questions(
                title=row['title'],
                question=row['question'],
                description=row['description'],
                sample_inputs=row['sample_inputs'],
                sample_outputs=row['sample_outputs'],
                test_cases=[jsonable_encoder(QuestionTestCase(**case)) for case in json.loads(row['test_cases'])] 
            )
            db.add(problem)
            added_q_count += 1
        db.commit()
        return {"message": f"Inserted {added_q_count} rows into 'Questions' table"}
    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail=f"{e.errors(include_url=False)}"
            )
    except Exception as e:
        raise e

@router.put("/update", response_model=QuestionResponse)
async def update_question(
    question_id:Annotated[int, Query()],
    update_body:Annotated[UpdateQuestion, Body()],
    db:Annotated[Session, Depends(get_db)],
):
    try:
        ## get the question
        db_question = db.query(Questions).filter(Questions.question_id == question_id).first()
        if not db_question:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                                detail=f"Question ID: {question_id} Not Fount")
        
        ##update the required fileds
        update_data = update_body.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_question, key, value)
        db.commit()
        return db_question
    except Exception as e:
        raise e
    
@router.get("/get", response_model=list[QuestionResponse])  
async def get_questions(
    db:Annotated[Session, Depends(get_db)],
    question_id:Annotated[int|None, Query()]= None,
):
    try:
        ## form base query
        base_query = db.query(Questions)

        ## check is qusetion id provided
        if question_id:
            base_query = base_query.filter(Questions.question_id == question_id)

        db_question = base_query.all()
        return db_question
    except Exception as e:
        raise e

@router.delete("/delete", status_code=status.HTTP_200_OK)
async def delete_question(
    db:Annotated[Session, Depends(get_db)],
    question_id:Annotated[int, Query()],
):
    try:
        ## check is question exsist
        db_question = db.query(Questions).filter(Questions.question_id == question_id).first()
        if not db_question:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Question ID: {question_id} Not Found"
            )
        
        ## delete the question
        db.delete(db_question)
        db.commit()
        return {"message":f"Question ID: {question_id} deleted successfully"}
    except Exception as e:
        raise e





