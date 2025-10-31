import tempfile
import shutil
from typing import Annotated
from fastapi import Query, Body
############################################

from ..utils.subprocessor import languages
from ..schemas.compiler_interpreter import CodeSubmit
############################################


## make file extension dict
file_extension = {
"python":".py",
"java":".java",
"php":".php"
}


## fuction to takes language and each question code, returns file paths for each question
async def code_push_toFile(
        language:Annotated[languages, Query()],
        request_body:Annotated[list[CodeSubmit], Body()],
):
        
        """
        fuction to takes language and each question code, 
        returns file paths for each question
        """

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

                file_paths += [[i["question_id"], tempf]]
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




