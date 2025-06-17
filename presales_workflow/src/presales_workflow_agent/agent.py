from contextlib import AsyncExitStack

from dotenv import load_dotenv
from google.adk import Agent
from google.adk.agents import SequentialAgent

from src.presales_workflow_agent.prompt.root_agent_prompt import \
    ROOT_AGENT_PROMPT
from src.presales_workflow_agent.sub_agent.document_analysis.agent import \
    create_document_analysis_manager_agent
from src.presales_workflow_agent.sub_agent.offering.agent import \
    create_offering_manager_agent
from src.presales_workflow_agent.sub_agent.research.agent import \
    create_research_manager_agent
from src.presales_workflow_agent.sub_agent.workshop.agent import \
    create_workshop_manager_agent
from src.shared.agent import knowledge_base_remote_agent_tool
from src.shared.config.model_config import GENERIC_MODEL
from src.shared.tool.get_artifact import get_existing_artifact
from src.shared.tool.list_artifacts import list_artifacts
from src.shared.tool.save_artifact import save_artifact

load_dotenv()


async def create_agent() -> tuple[Agent, AsyncExitStack]:
    research_manager_agent = await create_research_manager_agent()
    workshop_manager_agent = await create_workshop_manager_agent()
    document_analysis_manager_agent = await create_document_analysis_manager_agent()
    offering_manager_agent = await create_offering_manager_agent()

    presales_sequence_agent = SequentialAgent(
        sub_agents=[
            document_analysis_manager_agent,
            research_manager_agent,
            workshop_manager_agent,
            offering_manager_agent,
        ],
        name="presales_sequence_agent",
        description="Presales Process Sequence Agent",
    )

    agent = Agent(
        model=GENERIC_MODEL,
        description="Presales Workflow Agent",
        name="presales_workflow_agent",
        sub_agents=[presales_sequence_agent],
        instruction=ROOT_AGENT_PROMPT,
        tools=[
            save_artifact,
            knowledge_base_remote_agent_tool,
            get_existing_artifact,
            list_artifacts,
        ],
    )

    return agent, AsyncExitStack()


root_agent = create_agent()
