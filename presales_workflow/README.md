# Presales Workflow Agent

An AI-powered agent system designed to streamline and enhance the presales process for software development projects through a structured, multi-agent workflow.

## Overview

The Presales Workflow Agent orchestrates a comprehensive presales process by coordinating specialized sub-agents that collaboratively analyze requirements, research market conditions, design solutions, and create tailored offers. This system helps organizations respond to customer requests more efficiently while maintaining high-quality output.

## Agent Description

The Presales Workflow Agent is a sophisticated orchestrator that:

- Manages an end-to-end presales process from document analysis to offer creation
- Coordinates multiple specialized sub-agents working in sequence and parallel
- Maintains state through structured artifacts that are passed between agents
- Leverages both internal knowledge repositories and external information sources
- Produces comprehensive, high-quality presales documentation
- Adapts to various types of customer requirements and project scenarios
- Ensures consistency in approach and output across the presales process

The agent follows a structured four-stage workflow:
1. **Document Analysis**: Analyze customer documents to extract project requirements
2. **Research**: Gather market, competitor, and solution research
3. **Workshop**: Perform technical analysis and solution design from various perspectives
4. **Offering**: Create and refine offers based on the analysis and technical design

## Sub-Agents

The system utilizes the following specialized sub-agents:

| Agent | Description |
|-------|-------------|
| **Document Analysis Manager** | Analyzes customer documents and extracts project requirements |
| **Research Manager** | Coordinates research on market conditions, competitors, and existing solutions |
| **Workshop Manager** | Orchestrates technical analysis and solution design across disciplines |
| **Offering Manager** | Creates final offers based on the analysis and technical design |
| **Backend Development Agent** | Analyzes backend requirements and proposes technical solutions |
| **Frontend Development Agent** | Designs frontend architectures and interfaces |
| **Mobile Development Agent** | Evaluates mobile development needs and strategies |
| **DevOps Development Agent** | Plans infrastructure and deployment approaches |
| **Product Design Agent** | Creates product design concepts and specifications |
| **UX Agent** | Analyzes user experience aspects and requirements |
| **UI Agent** | Designs user interface concepts and visual elements |
| **Project Manager Agent** | Estimates timelines, resources, and project management approaches |
| **Solution Architect Agent** | Creates high-level solution architectures and integration strategies |
| **AI Solutions Agent** | Identifies AI opportunities and integration approaches |

## Development Setup

### Prerequisites

- Python 3.13+
- Poetry (for dependency management)
- Google API key (for ADK and LLM access)

### Environment Setup

1. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

2. Create a `.env` file by copying the example:
   ```bash
   cp .env.example .env
   ```

3. Edit the `.env` file and add your API keys and settings.

### Running the Service

You can start the service using one of the provided CLI commands:

```bash
# Start the web interface
poetry run start-web

# Start the API server
poetry run start-api
```

## Available CLI Commands

| Command | Description |
|---------|-------------|
| `start-web` | Starts the web interface for the Presales Workflow Agent |
| `start-api` | Starts the API server for programmatic access |

## Integration with Other Services

The Presales Workflow Agent integrates with:

- **Knowledge Base Agent**: Retrieves company experience and project information
- **Web Search**: Gathers external information about markets and competitors
- **FireCrawl MCP**: Provides web scraping capabilities for research

## Troubleshooting

If you encounter any issues:

1. Check that your API keys are valid and properly configured
2. Ensure all required environment variables are set correctly
3. Verify that any external services (Knowledge Base, etc.) are accessible

## License

This project is licensed under a Restricted Use License that allows for educational and research use while prohibiting commercial use without explicit permission. See the [LICENSE](../LICENSE) file for details.

For commercial licensing inquiries, please contact: konrad.jarzyna0@gmail.com
