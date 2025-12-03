from fastapi import APIRouter, HTTPException, status, Depends, Body, Query
from typing import Annotated, Optional
from sqlalchemy.orm import Session


from ..schemas.compiler_exam import ExamCreation, ExamCreationResponse, ExamUpdate, ExamQuestionResponse
from ..models.compiler import CodingExam, Questions, CandidateExamResult
from ..db import get_db



router = APIRouter(prefix="/exam", tags=["EXAM"])


@router.post("/creation", response_model=ExamCreationResponse)
async def exam_creation(
    request_body:Annotated[ExamCreation, Body(
        example=
            {
                "title": "technical",
                "description": "something....",
                "collage":"SMVM",
                "window_start": "2025-12-01T11:40:36.967Z",
                "window_end": "2025-12-01T12:40:36.967Z",
                "duration": 20,
                "category": "texc",
                "questions": {
                    "1": {
                    "question_bank_id": 2,
                    "score": 10
                    },
                    "2": {
                    "question_bank_id": 1,
                    "score": 10
                    },
                    "3": {
                    "question_bank_id": 3,
                    "score": 50
                    }
                }
            }
        
    )],
    db:Annotated[Session, Depends(get_db)],
):
    try:
        ## -----------------------------------------
        ## if you want do this task
        ## ----
        ## validate is provided questions are valid.
        ## i.e, check is quetion ids' are in questions table at server.

        ## get question ids' to check in Questions table at server
        all_question_ids = [i.question_bank_id for i in request_body.questions.values()]
        db_question_ids = [i.question_id for i in db.query(Questions).filter(Questions.question_id.in_(all_question_ids)).all()]

        ## list to catch not founf questions at db
        not_found_question_ids = []
        for i in all_question_ids:
            if i not in db_question_ids:
                not_found_question_ids += [i]

        if not_found_question_ids:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Quetion IDs: {not_found_question_ids} Not Found in Quetions table at server"
            )  
        ## -----------------------------------------

        ## After proper validation, add exam details at CodingExam Table.

        ### calculate duration    
        data = CodingExam(**request_body.model_dump())    
        db.add(data)
        db.commit()
        db.refresh(data)
        return data

        
    except Exception as e:
        raise e


@router.put("/update", response_model=ExamCreationResponse)
async def exam_update(
    exam_id:Annotated[int, Query()],
    request_body:Annotated[ExamUpdate, Body(
        example=
            {
                "title": "technical",
                "description": "something....",
                "collage":"SMVM",
                "is_active":1,
                "window_start": "2025-12-01T11:40:36.967Z",
                "window_end": "2025-12-01T12:40:36.967Z",
                "duration": 20,
                "category": "texc",
                "questions": {
                    "1": {
                    "question_bank_id": 2,
                    "score": 10
                    },
                    "2": {
                    "question_bank_id": 1,
                    "score": 10
                    },
                    "3": {
                    "question_bank_id": 3,
                    "score": 50
                    }
                }
            }
        
    )],
    db:Annotated[Session, Depends(get_db)],
):
    try:
        ## validate the examId
        db_coding_exam = db.query(CodingExam).filter(CodingExam.id == exam_id).first()
        if not db_coding_exam:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Exam ID: {exam_id} Not Found on Question table at server..."
            )
        
        ## get updated data
        request_body_dict = request_body.model_dump(exclude_defaults=True)
        if not request_body_dict:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Empty data not updatable..."
            )


        ## if questions are updating
        if "questions" in request_body_dict:
            ## -----------------------------------------
            ## if you want do this task
            ## ----
            ## validate is provided questions are valid.
            ## i.e, check is quetion ids' are in questions table at server.

            ## get question ids' to check in Questions table at server
            all_question_ids = [i.question_bank_id for i in request_body.questions.values()]
            db_question_ids = [i.question_id for i in db.query(Questions).filter(Questions.question_id.in_(all_question_ids)).all()]

            ## list to catch not founf questions at db
            not_found_question_ids = []
            for i in all_question_ids:
                if i not in db_question_ids:
                    not_found_question_ids += [i]

            if not_found_question_ids:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Quetion IDs: {not_found_question_ids} Not Found in Quetions table at server"
                )  
            ## -----------------------------------------    


        ## After proper validation, update the row.
        for col, val in request_body_dict.items():
            setattr(db_coding_exam, col, val)
        db.commit()

        return db_coding_exam
    except Exception as e:
        raise e


@router.get("/get", response_model=list[ExamCreationResponse])
async def get_exam(
    db:Annotated[Session, Depends(get_db)],
    exam_id:Annotated[int|None, Query()] = None,
    title:Annotated[str|None, Query()] = None,
    category:Annotated[str|None, Query()] = None,
    collage:Annotated[str|None, Query()] = None,
):
    try:
        ## create base query
        db_coding_exam_base = db.query(CodingExam)

        ## apply the results
        if exam_id:
            db_coding_exam_base = db_coding_exam_base.filter(CodingExam.id == exam_id)
        if title:
            db_coding_exam_base = db_coding_exam_base.filter(CodingExam.title.ilike(f"%{title}%"))
        if category:
            db_coding_exam_base = db_coding_exam_base.filter(CodingExam.category.ilike(f"%{category}%"))
        if collage:
            db_coding_exam_base = db_coding_exam_base.filter(CodingExam.collage.ilike(f"%{collage}%"))

        ## get final result
        db_coding_exam_final = db_coding_exam_base.all()

        return db_coding_exam_final

    except Exception as e:
        raise e



@router.delete("/delete", status_code=status.HTTP_200_OK)
async def delete_exam(
    exam_id:Annotated[int, Query()],
    db:Annotated[Session, Depends(get_db)],
):
    try:
        ## validate the examId
        db_coding_exam = db.query(CodingExam).filter(CodingExam.id == exam_id).first()
        if not db_coding_exam:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Exam ID: {exam_id} Not Found on Question table at server..."
            )
        
        ## Avoid deleting exam when its ID at results table
        if db.query(CandidateExamResult).filter(CandidateExamResult.exam_id == exam_id).first():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Not able to delete the exam ID: {exam_id}, some results are based on this exam ID"
            )
        
        ## del the exam
        db.delete(db_coding_exam)
        db.commit()
        return {"message":f"Exam ID: {exam_id} deleted successfully"}
    except Exception as e:
        raise e
    

@router.get("/get/details", response_model=ExamQuestionResponse)
async def get_exam(
    db:Annotated[Session, Depends(get_db)],
    exam_id:Annotated[int, Query()],
):
    try:
        ## validate the examId
        db_coding_exam = db.query(CodingExam).filter(CodingExam.id == exam_id).first()
        if not db_coding_exam:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Exam ID: {exam_id} Not Found on Question table at server..."
            )
        

        for exam_question, value in db_coding_exam.questions.items():
            ## get details from question bank
            details = db.query(Questions).filter(Questions.question_id == value["question_bank_id"]).first()

            ## push each bank question deatils into regarding exam question
            db_coding_exam.questions[exam_question]["details"] = details
        
        return db_coding_exam
    except Exception as e:
        raise e



 
####################### THIS ROUTER DONE BY RAHUL ###########################
@router.get("/results")
def get_results(
    db: Session = Depends(get_db),
    candidate_id: Optional[str] = Query(default=None),
    exam_id: Optional[int] = Query(default=None),
):
    try:
        query = db.query(CandidateExamResult)

        if candidate_id:
            query = query.filter(CandidateExamResult.candidate_id == candidate_id)
        if exam_id is not None:
            query = query.filter(CandidateExamResult.exam_id == exam_id)

        records = query.all()
 
        return records
 
    except Exception as e:
        raise e

##############################################################################





