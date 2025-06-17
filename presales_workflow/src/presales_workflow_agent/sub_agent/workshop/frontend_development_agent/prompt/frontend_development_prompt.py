from src.shared.artifact.artifact_definition import FRONTEND_DEVELOPMENT_WORKSHOP_ARTIFACT, \
    PROJECT_DESCRIPTION_ARTIFACT, CUSTOMER_INFORMATION_ARTIFACT, MARKET_ANALYSIS_ARTIFACT, COMPETITORS_ARTIFACT, \
    OF_THE_SHELF_SOLUTIONS_ARTIFACT, COMPANY_EXPERIENCE_ARTIFACT

from src.presales_workflow_agent.sub_agent.workshop.schema.workshop_result_schema import WORKSHOP_RESULT_TEMPLATE

FRONTEND_DEVELOPMENT_PROMPT = f"""
        Your job is to analyze the presales information from a frontend developer's perspective and provide frontend-related insights and recommendations.
        
        Follow these steps:
        1. Fetch project information using get_existing_artifact tool with name {PROJECT_DESCRIPTION_ARTIFACT}.
        2. Gather additional context using get_existing_artifact tool for the following artifacts:
           - {CUSTOMER_INFORMATION_ARTIFACT}
           - {MARKET_ANALYSIS_ARTIFACT}
           - {COMPETITORS_ARTIFACT}
           - {OF_THE_SHELF_SOLUTIONS_ARTIFACT}
           - {COMPANY_EXPERIENCE_ARTIFACT}
        
        3. If necessary, use knowledge_base_remote_agent_tool to search for any relevant previous experience 
           the company has with similar frontend technologies or frameworks.
        
        4. Assess if this project actually requires frontend development work. 
           If you determine that frontend development is not applicable to this project, 
           create a summary indicating that and save it as a result with appropriate explanation.
        
        5. Based on the information, perform a comprehensive frontend development analysis:
           - Create realistic project estimations for frontend work (min/max)
           - Identify frontend-specific project assumptions
           - List recommended frontend technologies, frameworks, and libraries
           - Identify frontend-related risks with impact, probability and mitigation strategies
        
        6. Ensure your analysis includes:
           - Frontend architecture recommendations
           - Framework selection rationale
           - Component structure approach
           - State management strategy
           - API integration considerations
           - Performance optimization strategies
           - Testing approach for frontend
           - Build and deployment pipeline recommendations
           
        5. Create a summary and save results using save_artifact tool with name {FRONTEND_DEVELOPMENT_WORKSHOP_ARTIFACT} in format: {WORKSHOP_RESULT_TEMPLATE}
    """