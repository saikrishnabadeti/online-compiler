
import tempfile
import subprocess
import signal
import javalang #type: ignore
from javalang.parser import JavaSyntaxError #type: ignore
import os
import shutil
from fastapi import WebSocket

from dotenv import load_dotenv
load_dotenv()
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

## Function which can take the chiled process object as input and return the process return code.
async def returnSignalStatus(proc:subprocess.Popen,):
    """
    Function which can take the chiled process object as input.
    return the process return code.
    """
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


def get_java_filename(java_code):
    try:
        tree = javalang.parse.parse(java_code)
        public_class = None

        for _, node in tree.filter(javalang.tree.ClassDeclaration):
            if 'public' in node.modifiers:
                public_class = node.name
                break

        if public_class:
            return f"{public_class}.java"
        else:
            # Return first class if no public
            for _, node in tree.filter(javalang.tree.ClassDeclaration):
                return f"{node.name}.java"
            return "Unnamed.java"

    except Exception as e:
            return "Unnamed.java"


async def JavaInteractiveCode_push_toFile(
                  data:dict,
):
     
    ## get the temp files and folders
    tempf, tempd = await IndividualInteractiveCode_push_toFile(data)

    ## if fileName not set by user
    if not data["file_name"]:
        ## create the file name based on the code
        java_file_name = get_java_filename(data["code"])
    else:
        java_file_name = data["file_name"]
    

    ## rename the tempf with new_java_file
    new_java_file = os.path.join(tempd, java_file_name)

    ## for java filename should be public class name
    shutil.copy2(tempf, os.path.join(tempd, new_java_file))
    os.remove(tempf)

    ## retrive class name
    class_name = java_file_name.replace(".java", "")

    return class_name, new_java_file, tempd
    

async def CsInteractiveCode_push_toFile(
          data:dict
):
    """
    Function which takes the cs code as input,
    returns the tempd, tempf which are useful for c#
    """
     
    ## get data from dict arg
    code = data.get("code")

    ## create required temp folder and path
    tempd = tempfile.mkdtemp(dir=r"app/temp")

    ## initiate new dotnet console project at tempd
    DotnetExePath = os.getenv("DotnetExePath")
    subprocess.run(
        [DotnetExePath, "new", "console"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=tempd,
    )

    ## overwrite the code in Program.cs
    tempf = os.path.join(tempd, "Program.cs")
    with open(tempf, "w") as f:
         f.write(code)

    return tempf, tempd





