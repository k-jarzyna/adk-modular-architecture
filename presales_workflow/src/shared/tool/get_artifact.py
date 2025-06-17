from google.adk.tools import ToolContext


async def get_existing_artifact(tool_context: ToolContext, artifact_name: str):
    try:
        return await tool_context.load_artifact(artifact_name)
    except FileNotFoundError:
        return f"Artifact '{artifact_name}' not found. Please ensure the artifact exists before attempting to access it."
    except PermissionError:
        return "Unable to access artifact due to permission restrictions."
    except Exception:
        return f"An error occurred while retrieving the artifact '{artifact_name}'. Please try again or check if the artifact exists."
