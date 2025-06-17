import subprocess
import os
import sys

def start_web():
    os.environ["PYTHONPATH"] = "."
    subprocess.run(["adk", "web", "src"], check=True)

def start_api():
    os.environ["PYTHONPATH"] = "."
    subprocess.run(["adk", "run", "src"], check=True)

def start_a2a():
    os.environ["PYTHONPATH"] = "."
    subprocess.run([sys.executable, "src/knowledge_base_agent/a2a_server.py"], check=True)