import subprocess
import os

def start_web():
    os.environ["PYTHONPATH"] = "."
    subprocess.run(["adk", "web", "src"], check=True)

def start_api():
    os.environ["PYTHONPATH"] = "."
    subprocess.run(["adk", "run", "src"], check=True)

def start_dev():
    os.environ["PYTHONPATH"] = "."
    subprocess.run([
        "watchmedo", "auto-restart",
        "--directory=.",
        "--pattern=*.py",
        "--recursive",
        "--",
        "adk", "web", "src"
    ], check=True)