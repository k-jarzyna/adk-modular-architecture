import os
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent
knowledge_base_a2a_address = os.environ.get("KNOWLEDGE_BASE_A2A_URL")

knowledge_agent = RemoteA2aAgent(
    name="knowledge_agent",
    description="Agent that handles checking company knowledge base.",
    agent_card=knowledge_base_a2a_address,
)