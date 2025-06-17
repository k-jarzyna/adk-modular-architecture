from google.adk import Agent

from src.presales_workflow_agent.sub_agent.workshop.ai_solutions_agent.prompt.ai_solutions_prompt import \
    AI_SOLUTIONS_PROMPT
from src.shared.agent import knowledge_base_remote_agent_tool
from src.shared.config.model_config import GENERIC_MODEL
from src.shared.tool.get_artifact import get_existing_artifact
from src.shared.tool.save_artifact import save_artifact

ai_solutions_agent = Agent(
    model=GENERIC_MODEL,
    name="ai_solutions_agent",
    description="Agent performing presales analysis from an AI/ML solutions perspective",
    instruction=AI_SOLUTIONS_PROMPT,
    tools=[get_existing_artifact, save_artifact, knowledge_base_remote_agent_tool],
)
