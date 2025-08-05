from google.adk.agents import ParallelAgent

from src.presales_workflow_agent.sub_agent.offering.internal_presales_summary_agent.agent import \
    internal_presales_summary_agent
from src.presales_workflow_agent.sub_agent.offering.mvp_offer_agent.agent import mvp_offer_agent
from src.presales_workflow_agent.sub_agent.offering.product_offer_agent.agent import product_offer_agent
from src.presales_workflow_agent.sub_agent.offering.services_offer_agent.agent import services_offer_agent
from src.presales_workflow_agent.sub_agent.offering.workshop_offer_agent.agent import workshop_offer_agent

offering_manager_agent = ParallelAgent(
    name="offering_manager_agent",
    description="Agent managing offering stage workflow",
    sub_agents=[
        mvp_offer_agent,
        workshop_offer_agent,
        services_offer_agent,
        product_offer_agent,
        internal_presales_summary_agent,
    ],
)
