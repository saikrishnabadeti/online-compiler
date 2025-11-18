from pydantic import BaseModel


## Run Test case response
class RunTestCaseResult(BaseModel):
    actual_inputs: str
    actual_outputs:str
    expected_outputs:str
    success:bool
    execution_time:float

class RunTestCaseResponse(BaseModel):
    message:str 
    test_case_result:list[RunTestCaseResult]

## questions submit

class CodeSubmit(BaseModel):
    question_id:int
    code:str ## when code is sending from frontend u should use escape(\) char to avoid josonify errors



## simple interperter result
class ProgrameExecutionResult(BaseModel):
    output:str
    error:str
    execution_time:float
