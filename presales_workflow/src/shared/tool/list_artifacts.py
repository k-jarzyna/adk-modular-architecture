from google.adk.tools import ToolContext


async def list_artifacts(tool_context: ToolContext):
    try:
        return await tool_context.list_artifacts()
    except Exception as e:
        return f"An unexpected error occurred during listing artifacts: {e}"
