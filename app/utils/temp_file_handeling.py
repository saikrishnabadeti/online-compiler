import tempfile
import shutil
from typing import Annotated
from fastapi import Query, Body, Depends, HTTPException, status
from sqlalchemy.orm import Session 
############################################

from ..utils.subprocessor import languages
from ..schemas.compiler_interpreter import CodeSubmit
from ..db import get_db
from ..models.compiler import CodingExam
############################################


## make file extension dict
file_extension = {
"python":".py",
"java":".java",
"php":".php",
"c":".c",
"cpp":".cpp",
"cs":".cs",
"nodejs":".js",
"bash":".sh",
}


## fuction to takes language and each question code, returns file paths for each question
async def code_push_toFile(
        exam_id:Annotated[int, Query()],
        language:Annotated[languages, Query()],
        request_body:Annotated[list[CodeSubmit], Body()],
        db:Annotated[Session, Depends(get_db)],
):
        
        """
        fuction to takes language and each question code, 
        returns file paths for each question
        """

        ## get exam data by its exam_id

        ## validate the examId
        db_coding_exam = db.query(CodingExam).filter(CodingExam.id == exam_id).first()
        if not db_coding_exam:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Exam ID: {exam_id} Not Found on Question table at server..."
            )
        questions_dict = db_coding_exam.questions
        

        ## map exam and blank question id


        file_suffix = file_extension[language]

        ## variable to store the paths of each temp file
        file_paths = []
        dir_paths = []
        for i in request_body:
                i = i.model_dump()
                ## create required temp folder and path
                tempd = tempfile.mkdtemp(dir=r"app/temp")
                tempf = tempfile.mkstemp(dir=tempd, suffix=file_suffix)[-1]

                ## push data into temp file
                with open(tempf, "w") as f:
                        f.write(i["code"])

                file_paths += [[(questions_dict[str(i["exam_question_id"])]["bank_question_id"]),i["exam_question_id"], tempf]]
                dir_paths += [tempd]
        
        ## return file paths
        yield file_paths



        ## remove the temp directory
        for i in dir_paths:
                shutil.rmtree(i)




## Function which takes language and only code, returns single file path
async def IndividualCode_push_toFile(
        language:Annotated[languages, Query()],
        code:Annotated[str, Body()],
):

        """
        Function which takes language and only code, 
        returns single file path
        """
        file_suffix = file_extension[language]

        
        ## create required temp folder and path
        tempd = tempfile.mkdtemp(dir=r"app/temp")
        tempf = tempfile.mkstemp(dir=tempd, suffix=file_suffix)[-1]

        ## push data into temp file
        with open(tempf, "w") as f:
                f.write(code)      

         ## return file paths
        yield tempf



        ## remove the temp directory
        shutil.rmtree(tempd)





