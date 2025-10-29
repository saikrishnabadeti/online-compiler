from sqlalchemy.orm import Session
from ..models.compiler import CandidateExamResult
from datetime import datetime
from zoneinfo import ZoneInfo

async def result_store(
        candidate_id:str,
        result:list[dict],
        db:Session,
):
    
    ## if row is existed on mentioned candidate in results table
    db_result = db.query(CandidateExamResult).filter(CandidateExamResult.candidate_id == candidate_id).first()
    if db_result:
        pass
        db_result.score += [{"time":datetime.now(ZoneInfo("Asia/Kolkata")).__str__(), "result": result}]


    ## if no row is existed on mentioned candidate in results table
    else:
        pass
        new_row = CandidateExamResult(candidate_id = candidate_id, score = [{"time":datetime.now(ZoneInfo("Asia/Kolkata")).__str__(), "result": result}])
        db.add(new_row)

    db.commit()
    return 



















