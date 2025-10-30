import os
import subprocess
from fastapi import HTTPException, status
from typing import Literal
from dotenv import load_dotenv
import time


## load env

load_dotenv()

languages = Literal['python', 'php', 'NodeJs', 'java']



async def execute_python_code(file_path, inputs=None, execution_timeout = None):
    """EXECUTE THE PYTHON CODE and RETURN THE PROCESS output/error"""
    try:
        ## prepare running
        ### python .exe file

        cmd = [os.getenv("PythonExePath"), file_path]
        process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, error = process.communicate(input=inputs, timeout=execution_timeout)
        return output.strip(), error.strip()
    
    except subprocess.TimeoutExpired:
        raise HTTPException(
            status_code=status.HTTP_504_GATEWAY_TIMEOUT,
            detail="Python execution timed out after 10 seconds"
        )
    except subprocess.CalledProcessError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"CalledProcessError: {e}"
        )
    except FileNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"FileNotFoundError: {e}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error: {e}"
        )

async def execute_php_code(file_path, inputs=None, execution_timeout = None):
    """EXECUTE THE PYTHON CODE and RETURN THE PROCESS output/error"""
    try:
        ## prepare running
        ### python .exe file

        cmd = [os.getenv("PhpExePath"), file_path]
        process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, error = process.communicate(input=inputs, timeout=execution_timeout)
        return output.strip(), error.strip()
    
    except subprocess.TimeoutExpired:
        raise HTTPException(
            status_code=status.HTTP_504_GATEWAY_TIMEOUT,
            detail="Python execution timed out after 10 seconds"
        )
    except subprocess.CalledProcessError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"CalledProcessError: {e}"
        )
    except FileNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"FileNotFoundError: {e}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error: {e}"
        )



async def handler(language, file_path, inputs = None):
    
    try:

        
        start_time = time.time()
        if language == "python":
            result = await execute_python_code(file_path, inputs, execution_timeout=300)
        elif language == "php":
            result = await execute_php_code(file_path, inputs, execution_timeout=300)
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Unsupported language: {language}"
            )
        execution_time = time.time() - start_time
        return result[0], result[1], execution_time
    except Exception as e:
        raise e



