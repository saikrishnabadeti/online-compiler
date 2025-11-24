from pydantic import BaseModel



### questions pydantic



class QuestionTestCase(BaseModel):
    testcase:int
    input:str
    output:str

class QuestionBase(BaseModel):
    title:str
    question:str
    description:str
    sample_inputs:str
    sample_outputs:str
    test_cases:list[QuestionTestCase]

class AddQuestion(QuestionBase):
    pass

class UpdateQuestion(QuestionBase):
    title:str|None = None
    question:str|None = None
    description:str|None = None
    sample_inputs:str|None = None
    sample_outputs:str|None = None
    test_cases:list[QuestionTestCase]|None = None

class GetQuestion(QuestionBase):
    question_id:int







