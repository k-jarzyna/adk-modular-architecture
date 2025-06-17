from google.adk.tools import ToolContext
from google.genai.types import Part


async def save_artifact(
    tool_context: ToolContext, filename: str, file_content: str
) -> str:
    report_artifact = Part(text=file_content, file_data=None, inline_data=None)

    try:
        await tool_context.save_artifact(filename=filename, artifact=report_artifact)
        return "Artifact saved successfully."
    except ValueError as e:
        return f"Error saving artifact: {e}"
    except Exception as e:
        return f"An unexpected error occurred during artifact save: {e}"
