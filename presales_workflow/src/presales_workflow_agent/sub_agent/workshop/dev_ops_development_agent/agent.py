from google.adk import Agent

from src.presales_workflow_agent.sub_agent.workshop.dev_ops_development_agent.prompt.devops_development_prompt import \
    DEV_OPS_DEVELOPMENT_PROMPT
from src.shared.agent import knowledge_base_remote_agent_tool
from src.shared.config.model_config import GENERIC_MODEL
from src.shared.tool.get_artifact import get_existing_artifact
from src.shared.tool.save_artifact import save_artifact


dev_ops_development_agent = Agent(
    model=GENERIC_MODEL,
    name="dev_ops_development_agent",
    description="Agent performing presales analysis from a DevOps/Infrastructure perspective",
    instruction=DEV_OPS_DEVELOPMENT_PROMPT,
    tools=[get_existing_artifact, save_artifact, knowledge_base_remote_agent_tool],
)
