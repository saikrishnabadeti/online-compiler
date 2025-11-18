from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from datetime import datetime

##############################################################

from ..models.compiler import Questions
from ..schemas.compiler_interpreter import RunTestCaseResult
from ..utils.subprocessor import  handler
from ..utils.results_dependency import result_store



##############################################################



async def compute_testcases(
    file_list:list, 
    db:Session,
    language:str,
):
    overall_results = []
    for i in file_list:
        ## get question_id and file_path
        question_id = i[0]
        file_path = i[-1]

        # get test cases
        db_question = db.query(Questions).filter(Questions.question_id == question_id).first()
        if not db_question:
            raise HTTPException(
                status_code= status.HTTP_404_NOT_FOUND,
                detail=f"Question ID: {question_id} not Found"
            )
        
        ## get test cases
        test_cases = db_question.test_cases

        ## storage variable for testcase result
        result = []

        ## run each test case
        for testcase in test_cases:
            testcase_input = testcase["input"]
            testcase_output = testcase["output"]
            interpreted_output, interpreted_error, execution_time = await handler(language=language, file_path=file_path, inputs=testcase_input)

            result += [RunTestCaseResult(
                actual_inputs=testcase_input,
                actual_outputs="Error" if interpreted_error else interpreted_output,
                expected_outputs= testcase_output,
                execution_time=execution_time,
                success=True if testcase_output == interpreted_output else False
                ).model_dump()]
            
        overall_results += [{"question_id":question_id, "result":result}]
    return overall_results

async def submit_backgroundTask(
    file_list:list, 
    db:Session,
    language:str,
    current_user:str,
    submited_time:datetime,

):
    ## get testcase results for each question
    overall_results = await compute_testcases(file_list=file_list, db=db, language=language)

    ## compute percentage for each question
    q_result = []
    for item in overall_results:
        question_id = item["question_id"]
        result = item["result"]

        passed_test_cases = 0
        for testcase in result:
            if testcase["success"]:
                passed_test_cases += 1
        ## cal percentage for each question
        percentage = (passed_test_cases/len(result)) *100

        ## save the result for each question
        q_result += [{"question_id": question_id, "percentage":percentage}]

    ## save data at database
    await result_store(candidate_id=current_user, result=q_result, db=db, submited_time=submited_time)

    return


        









