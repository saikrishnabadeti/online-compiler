from pydantic import BaseModel, model_validator
from typing import Optional
from datetime import datetime
from fastapi import HTTPException




from .compiler_question import QuestionBase




## schemas for exam crud operations

class ExamQuestion(BaseModel):
    question_bank_id:int
    score:float

class ExamQuestionBoth(BaseModel):
    question_bank_id:int
    score:float
    details:QuestionBase

class ExamBase(BaseModel):
    title:str
    description:str
    collage:Optional[str] = None
    window_start:datetime
    window_end:datetime
    duration:float
    category:str
    questions:dict[int,ExamQuestion]

    ## validate is dates are in crt order.
    @model_validator(mode = "after")
    def is_dates_crt_order(self):
        if not self.window_end > self.window_start:
            raise HTTPException(status_code=422, detail=f"window_start should be less then window_end")
        if self.duration <= 0:
            raise HTTPException(status_code=422, detail=f"duration time must be positive integer")
        
        time_diff =  (self.window_end - self.window_start).seconds/60
        if self.duration > time_diff:
            raise HTTPException(status_code=422, detail=f"duration value must not be greater then windows time difference ...")

        return self


class ExamCreation(ExamBase):
    pass

class ExamCreationResponse(ExamBase):
    id:int
    is_active:int

class ExamUpdate(ExamBase):
    title:Optional[str] = None
    description:Optional[str] = None
    collage:Optional[str] = None
    window_start:Optional[datetime] = None
    window_end:Optional[datetime] = None
    duration:Optional[float] = None
    category:Optional[str] = None
    is_active:Optional[int] = None
    questions:dict[int,ExamQuestion] | None = None


    ## validate is dates are in crt order.
    @model_validator(mode = "after")
    def is_dates_crt_order(self):
        if self.window_start:
            if not self.window_end:
                raise HTTPException(
                    status_code=422, detail=f"sholud or should not be pass both windows times"
                )
        if self.window_end:
            if not self.window_start:
                raise HTTPException(
                    status_code=422, detail=f"sholud or should not be pass both windows times"
                )
        
        if self.window_end and self.window_start:
            if not self.window_end > self.window_start:
                raise HTTPException(status_code=422, detail=f"window_start should be less then window_end")
            if self.duration <= 0:
                raise HTTPException(status_code=422, detail=f"duration time must be positive integer")
            
            time_diff =  (self.window_end - self.window_start).seconds/60
            if self.duration > time_diff:
                raise HTTPException(status_code=422, detail=f"duration value must not be greater then windows time difference ...")

        return self


## class specialy for get exam response along with each question details
class ExamQuestionResponse(ExamCreationResponse):
    questions:dict[int,ExamQuestionBoth]





