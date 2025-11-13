from fastapi import APIRouter, WebSocket, WebSocketDisconnect, WebSocketException, Path
from typing import Annotated
import pty
import subprocess
import os
import asyncio
import select
import shutil
import time
from dotenv import load_dotenv
load_dotenv()
####################################################################################


from ..utils.interactive_compiler import (
    IndividualInteractiveCode_push_toFile, 
    returnSignalStatus,
    JavaInteractiveCode_push_toFile,
    CsInteractiveCode_push_toFile,
    )
####################################################################################



router = APIRouter(prefix="/interactive-compiler")


@router.websocket("/python")
async def interactive_compiler(
    websocket:WebSocket,
):
    try:
        pass
        ## accept webconnection
        await websocket.accept()

        ## get initial data while new web connection done
        init_data = await websocket.receive_json()

        ## get the code saved file path
        tempf, tempd = await IndividualInteractiveCode_push_toFile(init_data)

        # Create PTY pair
        input_r_fd, input_w_fd = pty.openpty()
        output_r_fd, output_w_fd = pty.openpty()
        error_r_fd, error_w_fd = pty.openpty()

        ## get the code exe path
        PythonExePath = os.getenv("PythonExePath", "python3")

        # Launch a child process (can be any interactive program)
        proc = subprocess.Popen(
            [PythonExePath,"-u", tempf],
            stdin=input_w_fd,
            stdout=output_w_fd,
            stderr=error_w_fd,
            close_fds=True,
            cwd=tempd,
        )

        ## close the all write fd's
        os.close(input_w_fd)
        os.close(output_w_fd)
        os.close(error_w_fd)

        async def read_from_child():
            while True:
                ## check is client socket is on connection
                if "DISCONNECTED" in websocket.client_state.__str__():
                    break

                await asyncio.sleep(0.01)
                r, _, _ = select.select([output_r_fd, error_r_fd], [], [],0) 
                if output_r_fd in r:
                    try:
                        data = os.read(output_r_fd, 1024)
                    except OSError:
                        proc.terminate()
                        proc_return_code = await returnSignalStatus(proc=proc)
                        await websocket.send_text(proc_return_code)
                        await websocket.close()
                        break
                    except Exception as e:
                        print(f"Error while handling output_r_fd: {e}")
                    if not data:
                        break
                    await websocket.send_text(data.decode(errors="ignore"))
                elif error_r_fd in r:
                    try:
                        data = os.read(error_r_fd, 1024)
                    except OSError:
                        proc.terminate()
                        proc_return_code = await returnSignalStatus(proc=proc)
                        await websocket.send_text(proc_return_code)
                        await websocket.close()
                        break
                    except Exception as e:
                        print(f"Error while handling error_r_fd: {e}")
                    if not data:
                        break
                    await websocket.send_text(data.decode(errors="ignore"))

        async def read_from_client():
            async for message in websocket.iter_text():
                os.write(input_r_fd, message.encode())

    
        await asyncio.gather(read_from_child(), read_from_client())

    except Exception as e:
        print("WebSocket closed or error:", e)
    finally:
        shutil.rmtree(tempd)
        os.close(input_r_fd)
        os.close(output_r_fd)
        os.close(error_r_fd)
        proc.kill()
        proc.wait()

@router.websocket("/php")
async def interactive_compiler(
    websocket:WebSocket,
):
    try:
        pass
        ## accept webconnection
        await websocket.accept()

        ## get initial data while new web connection done
        init_data = await websocket.receive_json()

        ## get the code saved file path
        tempf, tempd = await IndividualInteractiveCode_push_toFile(init_data)

        # Create PTY pair
        input_r_fd, input_w_fd = pty.openpty()
        output_r_fd, output_w_fd = pty.openpty()
        error_r_fd, error_w_fd = pty.openpty()

        ## get the code exe path
        PhpExePath = os.getenv("PhpExePath", "php")

        ## prepare the cmd's to lanuch in subprocess
        php_cmd = [
            PhpExePath,
            "-d", "zend.exception_ignore_args=Off",
            "-d", "display_errors=1",
            "-d", "log_errors=0",
            "-d", "error_reporting=E_ALL",
            "-d", "html_errors=0",           # Plain text errors
            tempf
        ]

        # Launch a child process (can be any interactive program)
        proc = subprocess.Popen(
            # [PhpExePath,  tempf],
            php_cmd,
            stdin=input_w_fd,
            stdout=output_w_fd,
            stderr=error_w_fd,
            close_fds=True,
            cwd=tempd,
        )

        ## close the all write fd's
        os.close(input_w_fd)
        os.close(output_w_fd)
        os.close(error_w_fd)

        async def read_from_child():
            while True:
                ## check is client socket is on connection
                if "DISCONNECTED" in websocket.client_state.__str__():
                    break

                await asyncio.sleep(0.01)
                r, _, _ = select.select([output_r_fd, error_r_fd], [], [],0) 
                if output_r_fd in r:
                    try:
                        data = os.read(output_r_fd, 1024)
                    except OSError:
                        proc.terminate()
                        proc_return_code = await returnSignalStatus(proc=proc)
                        await websocket.send_text(proc_return_code)
                        await websocket.close()
                        break
                    except Exception as e:
                        print(f"Error while handling output_r_fd: {e}")
                    if not data:
                        break
                    await websocket.send_text(data.decode(errors="ignore"))
                elif error_r_fd in r:
                    try:
                        data = os.read(error_r_fd, 1024)
                    except OSError:
                        proc.terminate()
                        proc_return_code = await returnSignalStatus(proc=proc)
                        await websocket.send_text(proc_return_code)
                        await websocket.close()
                        break
                    except Exception as e:
                        print(f"Error while handling error_r_fd: {e}")
                    if not data:
                        break
                    await websocket.send_text(data.decode(errors="ignore"))

        async def read_from_client():
            async for message in websocket.iter_text():
                os.write(input_r_fd, message.encode())

    
        await asyncio.gather(read_from_child(), read_from_client())

    except Exception as e:
        print("WebSocket closed or error:", e)
    finally:
        shutil.rmtree(tempd)
        os.close(input_r_fd)
        os.close(output_r_fd)
        os.close(error_r_fd)
        proc.kill()
        proc.wait()


@router.websocket("/java")
async def interactive_compiler(
    websocket:WebSocket,
):
    try:
        pass
        ## accept webconnection
        await websocket.accept()
        
        ## get initial data while new web connection done
        init_data = await websocket.receive_json()

        ## get the className, filePath, TempDir for java
        class_name, tempf, tempd = await JavaInteractiveCode_push_toFile(init_data)


        # Create PTY pair
        input_r_fd, input_w_fd = pty.openpty()
        output_r_fd, output_w_fd = pty.openpty()
        error_r_fd, error_w_fd = pty.openpty()

        ## get the code exe path
        JavacExePath = os.getenv("JavacExePath", "javac")
        JavaExePath = os.getenv("JavaExePath", "java")

        #Launch a child process to compile the java file with javac
        proc = subprocess.Popen(
            [JavacExePath, tempf],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=tempd,
        )
        _, compile_error = proc.communicate()

        ## check is any compiler error
        if compile_error:
            proc_return_code = await returnSignalStatus(proc=proc)
            await websocket.send_text(compile_error.decode(errors="ignore"))
            await websocket.send_text(proc_return_code)
            await websocket.close()
            return



        # Launch a child process (can be any interactive program)
        proc = subprocess.Popen(
            [JavaExePath,  class_name],
            stdin=input_w_fd,
            stdout=output_w_fd,
            stderr=error_w_fd,
            close_fds=True,
            cwd=tempd,
        )

        ## close the all write fd's
        os.close(input_w_fd)
        os.close(output_w_fd)
        os.close(error_w_fd)

        async def read_from_child():
            while True:
                ## check is client socket is on connection
                if "DISCONNECTED" in websocket.client_state.__str__():
                    break

                await asyncio.sleep(0.01)
                r, _, _ = select.select([output_r_fd, error_r_fd], [], [],0) 
                if output_r_fd in r:
                    try:
                        data = os.read(output_r_fd, 1024)
                    except OSError:
                        proc.terminate()
                        proc_return_code = await returnSignalStatus(proc=proc)
                        await websocket.send_text(proc_return_code)
                        await websocket.close()
                        break
                    except Exception as e:
                        print(f"Error while handling output_r_fd: {e}")
                    if not data:
                        break
                    await websocket.send_text(data.decode(errors="ignore"))
                elif error_r_fd in r:
                    try:
                        data = os.read(error_r_fd, 1024)
                    except OSError:
                        proc.terminate()
                        proc_return_code = await returnSignalStatus(proc=proc)
                        await websocket.send_text(proc_return_code)
                        await websocket.close()
                        break
                    except Exception as e:
                        print(f"Error while handling error_r_fd: {e}")
                    if not data:
                        break
                    await websocket.send_text(data.decode(errors="ignore"))

        async def read_from_client():
            async for message in websocket.iter_text():
                os.write(input_r_fd, message.encode())

    
        await asyncio.gather(read_from_child(), read_from_client())

    except Exception as e:
        print("WebSocket closed or error:", e)
    finally:

        shutil.rmtree(tempd)
        os.close(input_r_fd)
        os.close(output_r_fd)
        os.close(error_r_fd)
        proc.kill()
        proc.wait()


@router.websocket("/c")
async def interactive_compiler(
    websocket:WebSocket,
):
    try:
        pass
        ## accept webconnection
        await websocket.accept()
        
        ## get initial data while new web connection done
        init_data = await websocket.receive_json()

        ## get the filePath, TempDir for java
        tempf, tempd = await IndividualInteractiveCode_push_toFile(init_data)


        # Create PTY pair
        input_r_fd, input_w_fd = pty.openpty()
        output_r_fd, output_w_fd = pty.openpty()
        error_r_fd, error_w_fd = pty.openpty()

        ## get the code exe path
        GccExePath = os.getenv("GccExePath", "gcc")

        #Launch a child process to compile the java file with javac
        proc = subprocess.Popen(
            [GccExePath, tempf, "-o", "exebytecode"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=tempd,
        )
        _, compile_error = proc.communicate()

        ## check is any compiler error
        if compile_error:
            proc_return_code = await returnSignalStatus(proc=proc)
            await websocket.send_text(compile_error.decode(errors="ignore"))
            await websocket.send_text(proc_return_code)
            await websocket.close()
            return



        # Launch a child process (can be any interactive program)
        proc = subprocess.Popen(
            ["./exebytecode"],
            stdin=input_w_fd,
            stdout=output_w_fd,
            stderr=error_w_fd,
            close_fds=True,
            cwd=tempd,
        )

        ## close the all write fd's
        os.close(input_w_fd)
        os.close(output_w_fd)
        os.close(error_w_fd)

        async def read_from_child():
            while True:
                ## check is client socket is on connection
                if "DISCONNECTED" in websocket.client_state.__str__():
                    break

                await asyncio.sleep(0.01)
                r, _, _ = select.select([output_r_fd, error_r_fd], [], [],0) 
                if output_r_fd in r:
                    try:
                        data = os.read(output_r_fd, 1024)

                    except OSError:
                        proc.terminate()
                        proc_return_code = await returnSignalStatus(proc=proc)
                        await websocket.send_text(proc_return_code)
                        await websocket.close()
                        break
                    except Exception as e:
                        print(f"Error while handling output_r_fd: {e}")
                    if not data:
                        break
                    await websocket.send_text(data.decode(errors="ignore"))
                elif error_r_fd in r:
                    try:
                        data = os.read(error_r_fd, 1024)
                    except OSError:
                        proc.terminate()
                        proc_return_code = await returnSignalStatus(proc=proc)
                        await websocket.send_text(proc_return_code)
                        await websocket.close()
                        break
                    except Exception as e:
                        print(f"Error while handling error_r_fd: {e}")
                    if not data:
                        break
                    await websocket.send_text(data.decode(errors="ignore"))

        async def read_from_client():
            async for message in websocket.iter_text():
                os.write(input_r_fd, message.encode())

    
        await asyncio.gather(read_from_child(), read_from_client())

    except Exception as e:
        print("WebSocket closed or error:", e)
    finally:
        shutil.rmtree(tempd)
        os.close(output_r_fd)
        os.close(error_r_fd)
        proc.kill()
        proc.wait()


@router.websocket("/cpp")
async def interactive_compiler(
    websocket:WebSocket,
):
    try:
        pass
        ## accept webconnection
        await websocket.accept()
        
        ## get initial data while new web connection done
        init_data = await websocket.receive_json()

        ## get the filePath, TempDir for cpp
        tempf, tempd = await IndividualInteractiveCode_push_toFile(init_data)


        # Create PTY pair
        input_r_fd, input_w_fd = pty.openpty()
        output_r_fd, output_w_fd = pty.openpty()
        error_r_fd, error_w_fd = pty.openpty()

        ## get the code exe path
        GppExePath = os.getenv("GppExePath", "g++")

        #Launch a child process to compile the java file with javac
        proc = subprocess.Popen(
            [GppExePath, tempf, "-o", "exebytecode"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=tempd,
        )
        _, compile_error = proc.communicate()

        ## check is any compiler error
        if compile_error:
            proc_return_code = await returnSignalStatus(proc=proc)
            await websocket.send_text(compile_error.decode(errors="ignore"))
            await websocket.send_text(proc_return_code)
            await websocket.close()
            return



        # Launch a child process (can be any interactive program)
        proc = subprocess.Popen(
            ["./exebytecode"],
            stdin=input_w_fd,
            stdout=output_w_fd,
            stderr=error_w_fd,
            close_fds=True,
            cwd=tempd,
        )

        ## close the all write fd's
        os.close(input_w_fd)
        os.close(output_w_fd)
        os.close(error_w_fd)

        async def read_from_child():
            while True:
                ## check is client socket is on connection
                if "DISCONNECTED" in websocket.client_state.__str__():
                    break

                await asyncio.sleep(0.01)
                r, _, _ = select.select([output_r_fd, error_r_fd], [], [],0) 
                if output_r_fd in r:
                    try:
                        data = os.read(output_r_fd, 1024)

                    except OSError:
                        proc.terminate()
                        proc_return_code = await returnSignalStatus(proc=proc)
                        await websocket.send_text(proc_return_code)
                        await websocket.close()
                        break
                    except Exception as e:
                        print(f"Error while handling output_r_fd: {e}")
                    if not data:
                        break
                    await websocket.send_text(data.decode(errors="ignore"))
                elif error_r_fd in r:
                    try:
                        data = os.read(error_r_fd, 1024)
                    except OSError:
                        proc.terminate()
                        proc_return_code = await returnSignalStatus(proc=proc)
                        await websocket.send_text(proc_return_code)
                        await websocket.close()
                        break
                    except Exception as e:
                        print(f"Error while handling error_r_fd: {e}")
                    if not data:
                        break
                    await websocket.send_text(data.decode(errors="ignore"))

        async def read_from_client():
            async for message in websocket.iter_text():
                os.write(input_r_fd, message.encode())

    
        await asyncio.gather(read_from_child(), read_from_client())

    except Exception as e:
        print("WebSocket closed or error:", e)
    finally:
        shutil.rmtree(tempd)
        os.close(output_r_fd)
        os.close(error_r_fd)
        proc.kill()
        proc.wait()



@router.websocket("/cs")
async def interactive_compiler(
    websocket:WebSocket,
):
    try:
        pass
        ## accept webconnection
        await websocket.accept()
        
        ## get initial data while new web connection done
        init_data = await websocket.receive_json()

        ## get the filepath and directory for c#, tempd is main part to run
        tempf, tempd = await CsInteractiveCode_push_toFile(init_data)


        # Create PTY pair
        input_r_fd, input_w_fd = pty.openpty()
        output_r_fd, output_w_fd = pty.openpty()
        error_r_fd, error_w_fd = pty.openpty()

        ## get the code exe path
        DotnetExePath = os.getenv("DotnetExePath", "dotnet")

        # Launch a child process (can be any interactive program)
        proc = subprocess.Popen(
            [DotnetExePath, "run"],
            stdin=input_w_fd,
            stdout=output_w_fd,
            stderr=error_w_fd,
            close_fds=True,
            cwd=tempd,
        )

        ## close the all write fd's
        os.close(input_w_fd)
        os.close(output_w_fd)
        os.close(error_w_fd)

        async def read_from_child():
            while True:
                ## check is client socket is on connection
                if "DISCONNECTED" in websocket.client_state.__str__():
                    break

                await asyncio.sleep(0.01)
                r, _, _ = select.select([output_r_fd, error_r_fd], [], [],0) 
                if output_r_fd in r:
                    try:
                        data = os.read(output_r_fd, 1024)

                    except OSError:
                        proc.terminate()
                        proc_return_code = await returnSignalStatus(proc=proc)
                        await websocket.send_text(proc_return_code)
                        await websocket.close()
                        break
                    except Exception as e:
                        print(f"Error while handling output_r_fd: {e}")
                    if not data:
                        break
                    await websocket.send_text(data.decode(errors="ignore"))
                elif error_r_fd in r:
                    try:
                        data = os.read(error_r_fd, 1024)
                    except OSError:
                        proc.terminate()
                        proc_return_code = await returnSignalStatus(proc=proc)
                        await websocket.send_text(proc_return_code)
                        await websocket.close()
                        break
                    except Exception as e:
                        print(f"Error while handling error_r_fd: {e}")
                    if not data:
                        break
                    await websocket.send_text(data.decode(errors="ignore"))

        async def read_from_client():
            async for message in websocket.iter_text():
                os.write(input_r_fd, message.encode())

    
        await asyncio.gather(read_from_child(), read_from_client())

    except Exception as e:
        print("WebSocket closed or error:", e)
    finally:
        shutil.rmtree(tempd)
        os.close(output_r_fd)
        os.close(error_r_fd)
        proc.kill()
        proc.wait()










