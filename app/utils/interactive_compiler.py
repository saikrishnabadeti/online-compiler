
import tempfile
import subprocess
import signal
###############################################################

from .temp_file_handeling import file_extension
###############################################################


## Function which takes language and only code, returns single file path for interactive compiler, not file delete logic
async def IndividualInteractiveCode_push_toFile(
        data:dict,
):

        """
        Function which takes language and only code, 
        returns single file path,
        No file delete logic
        """
        
        ## get data from dict arg
        code = data.get("code")
        language = data.get("language")
        file_suffix = file_extension[language]

        
        ## create required temp folder and path
        tempd = tempfile.mkdtemp(dir=r"app/temp")
        tempf = tempfile.mkstemp(dir=tempd, suffix=file_suffix)[-1]

        ## push data into temp file
        with open(tempf, "w") as f:
                f.write(code)      

        ## return file paths
        return tempf, tempd


async def returnSignalStatus(proc:subprocess.Popen,):
    if type(proc.returncode) == type(-1):
        if proc.returncode == 0:
            return "\n***Code Sussesfuly Executed***\n"
        elif proc.returncode < 0:
            signum = -proc.returncode
            signame = signal.strsignal(signum) 
            return f"\nRuntime Error: {signame} (core dumped)\n"
        else:
            return f"\nExited with code {proc.returncode}\n"
    else:
        return f"\nExited with code {proc.returncode}\n"







