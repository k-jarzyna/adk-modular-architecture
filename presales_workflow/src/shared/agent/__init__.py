from google.adk.tools.agent_tool import AgentTool

from src.shared.agent.knowledge_base_remote_agent import \
    knowledge_base_remote_agent
from src.shared.agent.web_search_agent import web_search_agent

web_search_agent_tool = AgentTool(web_search_agent)
knowledge_base_remote_agent_tool = AgentTool(knowledge_base_remote_agent)

__all__ = ["web_search_agent_tool", "knowledge_base_remote_agent_tool"]
