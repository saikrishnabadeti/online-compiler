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



router = APIRouter(prefix="/docker/interactive-compiler")


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
            [
                "docker", "run", "--rm",
                "-i",                    # keep STDIN interactive
                "-v", f"{tempd}:/sandbox",
                "-w", "/sandbox",
                "--pids-limit=128",
                "--memory=256m",
                "--cpus=0.5",
                "python:3.12",
                "python3", os.path.basename(tempf)
            ],
            stdin=input_w_fd,
            stdout=output_w_fd,
            stderr=error_w_fd,
            close_fds=True,
            # cwd=tempd,
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


@router.websocket("/bash")
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
        BashExePath = os.getenv("BashExePath", "bash")





        # Launch a child process (can be any interactive program)

#!/usr/bin/env bash
        cmd = f"docker run --rm -i  -v {tempd}:/sandbox -w /sandbox  bash:latest bash {os.path.basename(tempf)}"
        proc = subprocess.Popen(
            cmd,
            stdin=input_w_fd,
            stdout=output_w_fd,
            stderr=error_w_fd,
            close_fds=True,
            # cwd=tempd,
            shell=True,
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
                        ##--------------------------------
                        ## check is any buffered data
                        try:
                            data = os.read(error_r_fd, 1024)
                            await websocket.send_text(data.decode())
                            print(f"output_r_fd/Error: {data}")

                        except IOError:
                            pass
                        ##--------------------------------

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
        











