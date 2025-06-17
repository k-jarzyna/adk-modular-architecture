from google.adk import Agent

from src.presales_workflow_agent.sub_agent.workshop.solution_architect_agent.prompt.solution_architect_prompt import \
    SOLUTION_ARCHITECT_PROMPT
from src.shared.agent import knowledge_base_remote_agent_tool
from src.shared.config.model_config import GENERIC_MODEL
from src.shared.tool.get_artifact import get_existing_artifact
from src.shared.tool.save_artifact import save_artifact

solution_architect_agent = Agent(
    model=GENERIC_MODEL,
    name="solution_architect_agent",
    description="Agent performing solution architecture analysis based on other technical agents' work",
    instruction=SOLUTION_ARCHITECT_PROMPT,
    tools=[get_existing_artifact, save_artifact, knowledge_base_remote_agent_tool],
)
