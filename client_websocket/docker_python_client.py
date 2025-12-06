import websocket  # type: ignore
import json
import threading
import time
import sys


######### Optional file objects ##########
# You can use these if you want automated input/output via files
# i_file = open("client_websocket/inputs.txt", 'r')






def on_message(ws, message):
    """Callback when a message is received from the server (child process output)."""
    print(f"\n{message}", end="")
    # with open("client_websocket/outputs.txt", "a") as o_file:
    #     o_file.write(message)


def on_error(ws, error):
    """Callback when an error occurs."""
    print(f"[Error]: {error}")


def on_close(ws, close_status_code, close_reason):
    """Callback when the connection is closed."""
    print(f"[Connection closed] Code={close_status_code}, Reason={close_reason}")


def on_open(ws):
    """Callback when connection opens: send initial code, then start interactive input."""
    print("[Connected to server ✅]")

    ## get code from .py file
    with open("client_websocket/python_test.py") as f:
        code = f.read()

    # Step 1: Send initial JSON data
    init_data = {
        "code": code,
        "language": "python"
    }
    ws.send(json.dumps(init_data))
    # print(f"[Sent init JSON]: {init_data}")

    # Step 2: Start an input loop in a separate thread
    def send_user_input():
        print("\n👉 Type input to send to child process (Ctrl+C to exit):")
        while True:
            try:
                user_input = input()
                ws.send(user_input + "\n")
            except KeyboardInterrupt:
                print("\n[User exit]")
                ws.close()
                break
            except Exception as e:
                print(f"[Input error]: {e}")
                break

    threading.Thread(target=send_user_input, daemon=True).start()


def run_websocket_client():
    """Connect to backend and maintain WebSocket session."""
    websocket_url = "ws://127.0.0.1:8000/docker/interactive-compiler/python"

    ws = websocket.WebSocketApp(
        websocket_url,
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )

    # Keep it running forever
    ws.run_forever(ping_interval=30, ping_timeout=10)


if __name__ == "__main__":
    run_websocket_client()
