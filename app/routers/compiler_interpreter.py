from fastapi import APIRouter, Query, Depends, Body, BackgroundTasks, HTTPException, status
from typing import Annotated
from sqlalchemy.orm import Session
from datetime import datetime
from zoneinfo import ZoneInfo
##########################################################

from ..utils.temp_file_handeling import code_push_toFile, IndividualCode_push_toFile
from ..utils.subprocessor import languages, handler
from ..utils.compiler_interpreter import compute_testcases, submit_backgroundTask
from ..db import get_db
from ..models.compiler import CandidateExamResult
from ..schemas.compiler_interpreter import ProgrameExecutionResult
##########################################################


router = APIRouter(prefix="/interpreter", tags=["INTERPRETER"])


@router.post("/execute-programe", response_model=ProgrameExecutionResult)
async def simple_compilation(
    language:Annotated[languages, Query()],
    file_path:Annotated[str, Depends(IndividualCode_push_toFile)],
    user_input:Annotated[str|None, Body()] = None,
    current_user:str = "S0001", ## make this as jwt dependency
):
    try:
        output, error, execution_time = await handler(language=language, file_path=file_path, inputs=user_input)
        return ProgrameExecutionResult(
            output=output,
            error=error,
            execution_time=execution_time
        )
    except Exception as e:
        raise e


@router.post("/test_cases")
async def run_test_case(
    language:Annotated[languages, Query()],
    file_list:Annotated[list, Depends(code_push_toFile)],
    db:Annotated[Session, Depends(get_db)],
    current_user:str = "S0001", ## make this as jwt dependency
):
    try:
        overall_results = await compute_testcases(file_list=file_list, db=db, language=language)
        return overall_results
    except Exception as e:
        raise e
    
@router.post("/submit")
async def submit_results(
    backgroundTask:BackgroundTasks,
    language:Annotated[languages, Query()],
    file_list:Annotated[list, Depends(code_push_toFile)],
    db:Annotated[Session, Depends(get_db)],
    exam_id:Annotated[int, Query()],
    current_user:str = "S0001", ## make this as jwt dependency
):
    try:
        ## check is candidate results alredy submited
        if db.query(CandidateExamResult).filter(
            CandidateExamResult.candidate_id == current_user,
            CandidateExamResult.exam_id == exam_id).first():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Result already submited for Candidate ID: {current_user} on exam ID: {exam_id}"
            )
        
        ## create background task to save the results at
        submited_time = datetime.now(ZoneInfo("Asia/Kolkata"))
        backgroundTask.add_task(submit_backgroundTask,file_list,db,language,current_user,submited_time,exam_id)
        return {"message":"successfully submited!!"}
    except Exception as e:
        raise e
