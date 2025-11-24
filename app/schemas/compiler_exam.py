from pydantic import BaseModel
from typing import Optional
from datetime import datetime





## schemas for exam crud operations

class ExamQuestion(BaseModel):
    blank_question_id:int
    score:float

class ExamBase(BaseModel):
    title:str
    description:str
    window_start:datetime
    window_end:datetime
    duration:float
    category:str
    questions:dict[int,ExamQuestion]


class ExamCreation(ExamBase):
    pass

class ExamCreationResponse(ExamBase):
    id:int

class ExamUpdate(ExamBase):
    title:Optional[str] = None
    description:Optional[str] = None
    window_start:Optional[datetime] = None
    window_end:Optional[datetime] = None
    duration:Optional[float] = None
    category:Optional[str] = None
    questions:dict[int,ExamQuestion] | None = None


