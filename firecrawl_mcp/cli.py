import subprocess
import os
import sys


def start_mcp():
    os.environ["PYTHONPATH"] = "."
    subprocess.run([sys.executable, "src/server.py"], check=True)