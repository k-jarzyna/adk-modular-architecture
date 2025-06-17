from google.adk import Agent

from src.presales_workflow_agent.sub_agent.offering.mvp_offer_agent.prompt.mvp_offer_prompt import \
    MVP_OFFER_PROMPT
from src.shared.agent import knowledge_base_remote_agent_tool
from src.shared.config.model_config import GENERIC_MODEL
from src.shared.tool.get_artifact import get_existing_artifact
from src.shared.tool.save_artifact import save_artifact


async def create_mvp_offer_agent() -> Agent:
    return Agent(
        model=GENERIC_MODEL,
        name="mvp_offer_agent",
        description="Agent generating an MVP (Minimum Viable Product) offer based on collected artifacts",
        instruction=MVP_OFFER_PROMPT,
        tools=[get_existing_artifact, save_artifact, knowledge_base_remote_agent_tool],
    )
