import os
from contextlib import AsyncExitStack

from google.adk.tools.mcp_tool import MCPTool, MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import SseServerParams

mcp_address = os.environ.get("WEB_SCRAPPER_MCP_URL")


def get_web_scrapper_tools() -> MCPToolset:
    return MCPToolset(
        connection_params=SseServerParams(url=mcp_address),
    )
