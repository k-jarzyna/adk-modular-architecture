from google.adk import Agent

from src.presales_workflow_agent.sub_agent.offering.internal_presales_summary_agent.prompt.internal_summary_prompt import \
    INTERNAL_SUMMARY_PROMPT
from src.shared.agent import knowledge_base_remote_agent_tool
from src.shared.config.model_config import GENERIC_MODEL
from src.shared.tool.get_artifact import get_existing_artifact
from src.shared.tool.save_artifact import save_artifact


internal_presales_summary_agent = Agent(
    model=GENERIC_MODEL,
    name="internal_presales_summary_agent",
    description="Agent creating an internal summary of the entire presales process for company use",
    instruction=INTERNAL_SUMMARY_PROMPT,
    tools=[get_existing_artifact, save_artifact, knowledge_base_remote_agent_tool],
)
