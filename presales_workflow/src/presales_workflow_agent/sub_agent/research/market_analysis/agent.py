from google.adk import Agent

from src.presales_workflow_agent.sub_agent.research.market_analysis.prompt.market_analysis_prompt import \
    MARKET_ANALYSIS_PROMPT
from src.shared.agent import web_search_agent_tool
from src.shared.config.model_config import GENERIC_MODEL
from src.shared.tool.get_artifact import get_existing_artifact
from src.shared.tool.save_artifact import save_artifact


market_analysis_agent = Agent(
    model=GENERIC_MODEL,
    name="market_analysis_agent",
    description="Agent providing market analysis capabilities.",
    instruction=MARKET_ANALYSIS_PROMPT,
    tools=[get_existing_artifact, web_search_agent_tool, save_artifact],
)
