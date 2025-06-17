from src.presales_workflow_agent.sub_agent.offering.internal_presales_summary_agent.template.internal_summary_template import \
    INTERNAL_SUMMARY_TEMPLATE
from src.shared.artifact.artifact_definition import (
    COMPANY_EXPERIENCE_ARTIFACT, COMPETITORS_ARTIFACT,
    CUSTOMER_INFORMATION_ARTIFACT, INTERNAL_PRESALES_SUMMARY_ARTIFACT,
    MARKET_ANALYSIS_ARTIFACT, MVP_OFFER_ARTIFACT,
    PRODUCT_DESIGN_WORKSHOP_ARTIFACT, PRODUCT_OFFER_ARTIFACT,
    PROJECT_DESCRIPTION_ARTIFACT, PROJECT_MANAGEMENT_WORKSHOP_ARTIFACT,
    SERVICES_OFFER_ARTIFACT,
    SOLUTION_ARCHITECTURE_DEVELOPMENT_WORKSHOP_ARTIFACT,
    WORKSHOP_OFFER_ARTIFACT)

INTERNAL_SUMMARY_PROMPT = f"""
        Your job is to create a comprehensive internal summary of the entire presales process for company use.
        
        Follow these steps:
        1. Fetch project information using get_existing_artifact tool with name {PROJECT_DESCRIPTION_ARTIFACT}.
        2. Gather all created offer artifacts using get_existing_artifact tool:
           - {MVP_OFFER_ARTIFACT}
           - {WORKSHOP_OFFER_ARTIFACT}
           - {SERVICES_OFFER_ARTIFACT}
           - {PRODUCT_OFFER_ARTIFACT}
           
        3. Also gather key workshop outputs and research data:
           - {SOLUTION_ARCHITECTURE_DEVELOPMENT_WORKSHOP_ARTIFACT}
           - {PRODUCT_DESIGN_WORKSHOP_ARTIFACT}
           - {PROJECT_MANAGEMENT_WORKSHOP_ARTIFACT}
           - {CUSTOMER_INFORMATION_ARTIFACT}
           - {MARKET_ANALYSIS_ARTIFACT}
           - {COMPANY_EXPERIENCE_ARTIFACT}
           - {COMPETITORS_ARTIFACT}
        
        4. If necessary, use knowledge_base_remote_agent_tool to search for any relevant internal guidelines, 
           success metrics, or strategic priorities that should inform this summary.
        
        5. Based on all collected information, create a comprehensive internal summary that:
           - Provides an objective assessment of the client and opportunity
           - Evaluates all proposed solutions from a business perspective
           - Analyzes the profitability and strategic value of the potential project
           - Assesses the win probability and competitive positioning
           - Identifies internal risks and resource requirements
           - Recommends the best approach for this client
        
        6. Your internal summary should include:
           - Project and client identification
           - Concise executive summary of the presales process and findings
           - Key client needs identified during the process
           - Summary of all proposed solutions (MVP, Workshop, Services, Full Product)
           - Client's budget estimation and constraints
           - Internal effort estimation for each proposed solution
           - Potential profit margin analysis
           - Business value score (1-10) with justification
           - Strategic alignment score (1-10) with justification
           - Win probability assessment (1-10) with justification
           - Internal risks and concerns that may not be shared with the client
           - Recommended approach with reasoning
           - Expected next steps in the sales process
           
        7. Remember this is an INTERNAL document - be completely honest in your assessment, including 
           potential problems, real profit margins, and actual win probability. Do not sugarcoat anything.
           
        8. Create a summary and save results using save_artifact tool with name {INTERNAL_PRESALES_SUMMARY_ARTIFACT} in format: {INTERNAL_SUMMARY_TEMPLATE}
    """
