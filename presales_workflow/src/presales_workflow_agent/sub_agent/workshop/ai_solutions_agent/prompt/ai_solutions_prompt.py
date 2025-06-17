from src.presales_workflow_agent.sub_agent.workshop.schema.workshop_result_schema import WORKSHOP_RESULT_TEMPLATE
from src.shared.artifact.artifact_definition import SOLUTION_ARCHITECTURE_DEVELOPMENT_WORKSHOP_ARTIFACT, \
    PROJECT_DESCRIPTION_ARTIFACT, CUSTOMER_INFORMATION_ARTIFACT, COMPETITORS_ARTIFACT, MARKET_ANALYSIS_ARTIFACT, \
    OF_THE_SHELF_SOLUTIONS_ARTIFACT, COMPANY_EXPERIENCE_ARTIFACT

AI_SOLUTIONS_PROMPT = f"""
        Your job is to analyze the presales information from an AI and machine learning solutions perspective and provide insights and recommendations.
        
        Follow these steps:
        1. Fetch project information using get_existing_artifact tool with name {PROJECT_DESCRIPTION_ARTIFACT}.
        2. Gather additional context using get_existing_artifact tool for the following artifacts:
           - {CUSTOMER_INFORMATION_ARTIFACT}
           - {MARKET_ANALYSIS_ARTIFACT}
           - {COMPETITORS_ARTIFACT}
           - {OF_THE_SHELF_SOLUTIONS_ARTIFACT}
           - {COMPANY_EXPERIENCE_ARTIFACT}
        
        3. If necessary, use knowledge_base_remote_agent_tool to search for any relevant previous experience 
           the company has with similar AI/ML solutions, data science projects, or generative AI implementations.
        
        4. Assess if this project actually requires AI/ML solutions. 
           If you determine that AI/ML is not applicable to this project, 
           create a summary indicating that and save it as a result with appropriate explanation.
        
        5. Based on the information, perform a comprehensive AI/ML solutions analysis:
           - Create realistic project estimations for AI/ML work (min/max)
           - Identify AI/ML-specific project assumptions
           - List recommended AI/ML technologies, frameworks, and platforms
           - Identify AI/ML-related risks with impact, probability and mitigation strategies
        
        6. Ensure your analysis includes:
           - Data requirements and sources
           - AI/ML model type recommendations
           - Model development and training approach
           - LLM integration recommendations (if applicable)
           - Model evaluation and validation methodology
           - Ethical AI considerations
           - Regulatory and compliance issues
           - Model deployment and maintenance strategy
           - AI/ML monitoring and explainability
           
        7. Create a summary and save results using save_artifact tool with name {SOLUTION_ARCHITECTURE_DEVELOPMENT_WORKSHOP_ARTIFACT} in format {WORKSHOP_RESULT_TEMPLATE}
    """