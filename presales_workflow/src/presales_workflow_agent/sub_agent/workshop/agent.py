from google.adk.agents import ParallelAgent, SequentialAgent

from src.presales_workflow_agent.sub_agent.workshop.ai_solutions_agent import \
    ai_solutions_agent
from src.presales_workflow_agent.sub_agent.workshop.backend_development_agent import \
    backend_development_agent
from src.presales_workflow_agent.sub_agent.workshop.dev_ops_development_agent import \
    dev_ops_development_agent
from src.presales_workflow_agent.sub_agent.workshop.frontend_development_agent import \
    frontend_development_agent
from src.presales_workflow_agent.sub_agent.workshop.mobile_development_agent import \
    mobile_development_agent
from src.presales_workflow_agent.sub_agent.workshop.product_design_agent import \
    product_design_agent
from src.presales_workflow_agent.sub_agent.workshop.project_manager_agent import \
    project_manager_agent
from src.presales_workflow_agent.sub_agent.workshop.solution_architect_agent import \
    solution_architect_agent


technical_agents = ParallelAgent(
        name="technical_agents",
        description="Group of technical agents working in parallel",
        sub_agents=[
            project_manager_agent,
            product_design_agent,
            frontend_development_agent,
            backend_development_agent,
            mobile_development_agent,
            dev_ops_development_agent,
            ai_solutions_agent,
        ],
    )

workshop_manager_agent = SequentialAgent(
    name="workshop_manager_agent",
    description="Agent managing workshop stage workflow in sequence",
    sub_agents=[technical_agents, solution_architect_agent],
)