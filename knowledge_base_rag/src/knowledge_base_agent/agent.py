import os

from dotenv import load_dotenv
from google.adk import Agent
from google.adk.a2a.utils.agent_card_builder import AgentCardBuilder
from google.adk.a2a.utils.agent_to_a2a import to_a2a
from google.genai.types import GenerateContentConfig

from src.knowledge_base_agent.prompt.prompt import KNOWLEDGE_BASE_AGENT_PROMPT
from src.knowledge_base_agent.tool.import_document import import_document
from src.knowledge_base_agent.tool.search_company_knowledge_base import \
    search_company_knowledge_base

load_dotenv()


from google.adk.models import Gemini
from google.genai import types

GENERIC_LLM_MODEL = os.environ.get("GENERIC_LLM_MODEL")

GENERIC_MODEL = Gemini(
    model=GENERIC_LLM_MODEL,
    retry_options=types.HttpRetryOptions(
        initial_delay=5,
        attempts=5,
    )
)


root_agent = Agent(
    model=GENERIC_MODEL,
    name="knowledge_base_agent",
    description="A knowledge base agent that can be used to answer questions about the software company experience and previous projects.",
    instruction=KNOWLEDGE_BASE_AGENT_PROMPT,
    generate_content_config=GenerateContentConfig(temperature=0.8),
    tools=[search_company_knowledge_base, import_document],
)

print(AgentCardBuilder(agent=root_agent).build())