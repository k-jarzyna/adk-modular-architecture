from src.presales_workflow_agent.sub_agent.offering.schema.offer_template import \
    OFFER_TEMPLATE
from src.shared.artifact.artifact_definition import (
    CUSTOMER_INFORMATION_ARTIFACT, MARKET_ANALYSIS_ARTIFACT,
    PRODUCT_DESIGN_WORKSHOP_ARTIFACT, PROJECT_DESCRIPTION_ARTIFACT,
    PROJECT_MANAGEMENT_WORKSHOP_ARTIFACT,
    SOLUTION_ARCHITECTURE_DEVELOPMENT_WORKSHOP_ARTIFACT,
    WORKSHOP_OFFER_ARTIFACT)

WORKSHOP_OFFER_PROMPT = f"""
        Your job is to create a tailored workshop offer for the client that will help them better define their product needs.
        
        Follow these steps:
        1. Fetch project information using get_existing_artifact tool with name {PROJECT_DESCRIPTION_ARTIFACT}
        2. Gather all key workshop outputs using get_existing_artifact tool for the following artifacts:
           - {SOLUTION_ARCHITECTURE_DEVELOPMENT_WORKSHOP_ARTIFACT}
           - {PRODUCT_DESIGN_WORKSHOP_ARTIFACT}
           - {PROJECT_MANAGEMENT_WORKSHOP_ARTIFACT}
           
        3. Also gather additional context using get_existing_artifact tool:
           - {CUSTOMER_INFORMATION_ARTIFACT}
           - {MARKET_ANALYSIS_ARTIFACT}
        
        4. If necessary, use knowledge_base_remote_agent_tool to search for any relevant previous experience 
           the company has with similar discovery workshops and facilitation.
        
        5. Based on all collected information, create a comprehensive workshop offer that:
           - Proposes a structured series of workshops to better define the client's product vision
           - Identifies key areas that need further exploration before full project commitment
           - Outlines a clear methodology for discovery and requirements refinement
           - Provides realistic budget and timeline estimations for the workshop phase
           - Shows clear deliverables from the workshop that will help inform future development
        
        6. Your workshop offer should include:
           - A compelling title and description focused on the discovery workshop approach
           - Clear budget estimates (with minimum and maximum ranges)
           - Realistic timeline (with minimum and maximum ranges in days/weeks)
           - List of specific workshop modules and activities included
           - Key benefits for the client choosing the workshop approach first
           - Important assumptions about the workshop process
           - Potential risks and mitigations for the workshop approach
           - Proposed facilitators and experts for the workshops
           - Clear next steps if the client decides to proceed with the workshops
           
        7. Create a summary and save results using save_artifact with name {WORKSHOP_OFFER_ARTIFACT} in format {OFFER_TEMPLATE}
    """
