import os

from dotenv import load_dotenv
from google.adk import Agent
from google.genai.types import GenerateContentConfig

from src.knowledge_base_agent.prompt.prompt import KNOWLEDGE_BASE_AGENT_PROMPT
from src.knowledge_base_agent.tool.import_document import import_document
from src.knowledge_base_agent.tool.search_company_knowledge_base import \
    search_company_knowledge_base

load_dotenv()

root_agent = Agent(
    model=os.environ.get("GENERIC_LLM_MODEL"),
    name="knowledge_base_agent",
    description="A knowledge base agent that can be used to answer questions about the software company experience and previous projects.",
    instruction=KNOWLEDGE_BASE_AGENT_PROMPT,
    generate_content_config=GenerateContentConfig(temperature=0.8),
    tools=[search_company_knowledge_base, import_document],
)
