import subprocess
import os
import sys

import dotenv

dotenv.load_dotenv()

A2A_SERVER_PORT = os.environ.get("A2A_SERVER_PORT")

def start_web():
    os.environ["PYTHONPATH"] = "."
    subprocess.run(["adk", "web", "src"], check=True)

def start_api():
    os.environ["PYTHONPATH"] = "."
    subprocess.run(["adk", "run", "src"], check=True)

def start_a2a():
    os.environ["PYTHONPATH"] = "."
    subprocess.run(["adk", "api_server", "src", "--a2a", "--port", f"{A2A_SERVER_PORT}"], check=True)
