from fastapi import APIRouter, Query, Depends, BackgroundTasks
from typing import Annotated
from sqlalchemy.orm import Session
from datetime import datetime
from zoneinfo import ZoneInfo
##########################################################

from ..utils.temp_file_handeling import code_push_toFile
from ..utils.subprocessor import languages
from ..utils.compiler_interpreter import compute_testcases, submit_backgroundTask
from ..db import get_db
##########################################################


router = APIRouter(prefix="/interpreter")


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
    current_user:str = "S0001", ## make this as jwt dependency
):
    try:
        ## create background task to save the results at
        submited_time = datetime.now(ZoneInfo("Asia/Kolkata"))
        backgroundTask.add_task(submit_backgroundTask,file_list,db,language,current_user,submited_time)
        return {"message":"successfully submited!!"}
    except Exception as e:
        raise e



