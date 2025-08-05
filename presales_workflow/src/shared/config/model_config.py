import os

from google.adk.models import Gemini
from google.genai import types

GENERIC_LLM_MODEL = os.environ.get("GENERIC_LLM_MODEL")

GENERIC_MODEL = Gemini(
    model=GENERIC_LLM_MODEL,
    retry_options=types.HttpRetryOptions(
        initial_delay=5,
        attempts=5,
    )
)
