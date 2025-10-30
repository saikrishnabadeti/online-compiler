from sqlalchemy.orm import Session
from datetime import datetime
from zoneinfo import ZoneInfo
#####################################################

from ..models.compiler import CandidateExamResult
####################################################

async def result_store(
        candidate_id:str,
        result:list[dict],
        db:Session,
        submited_time:datetime = datetime.now(ZoneInfo("Asia/Kolkata"))
):
    
    ## save the candidate results
    new_row = CandidateExamResult(candidate_id = candidate_id, score = [{"time":submited_time.__str__(), "result": result}])
    db.add(new_row)
    db.commit()
    return 



















