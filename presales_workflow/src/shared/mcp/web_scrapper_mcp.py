import os
from contextlib import AsyncExitStack

from google.adk.tools.mcp_tool import MCPTool, MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import SseServerParams

mcp_address = os.environ.get("WEB_SCRAPPER_MCP_URL")


async def get_web_scrapper_tools() -> list[MCPTool]:
    common_exit_stack = AsyncExitStack()

    tools, _ = await MCPToolset.from_server(
        connection_params=SseServerParams(url=mcp_address),
        async_exit_stack=common_exit_stack,
    )

    return tools
