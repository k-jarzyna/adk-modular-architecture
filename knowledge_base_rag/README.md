# Knowledge Base RAG Agent

A specialized knowledge agent designed to provide accurate and structured information about a company's experience and previous projects using Retrieval-Augmented Generation (RAG).

## Overview

The Knowledge Base RAG Agent serves as a company knowledge repository, allowing users to query historical project information and company experience. It uses vector-based similarity search to retrieve relevant information and provides concise, factual responses based solely on stored knowledge.

## Agent Description

The Knowledge Base Agent is a specialized assistant that:

- Provides accurate information about the company's experience and previous projects
- Supports storing new information about projects or accomplishments
- Retrieves relevant knowledge based on user queries
- Only responds with verified information found in the knowledge base
- Maintains an objective and professional tone
- Never fabricates or assumes details not found in the knowledge base
- Provides concise summaries of findings in well-formed sentences

This agent is particularly useful for:
- Accessing institutional knowledge about past projects
- Finding relevant company experience for new opportunities
- Maintaining a consistent knowledge repository for the organization
- Supporting presales activities with accurate information about company capabilities

## Development Setup

### Prerequisites

- Python 3.13+
- Poetry (for dependency management)
- Google API key or OpenAI API key (for LLM access)

### Environment Setup

1. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

2. Create a `.env` file by copying the example:
   ```bash
   cp .env.example .env
   ```

3. Edit the `.env` file and add your API keys:
   ```
   GOOGLE_GENAI_USE_VERTEXAI=FALSE
   GOOGLE_API_KEY=your_google_api_key_here
   
   GENERIC_LLM_MODEL=gemini-2.0-flash
   
   OPENAI_API_KEY=your_openai_api_key_here
   
   A2A_SERVER_PROTOCOL=http
   A2A_SERVER_PORT=6000
   A2A_SERVER_HOST=0.0.0.0
   ```

### Running the Service

You can start the service using one of the provided CLI commands:

```bash
# Start the web interface
poetry run start-web

# Start the API server
poetry run start-api

# Start the Agent-to-Agent (A2A) server
poetry run start-a2a
```

## Available CLI Commands

| Command | Description |
|---------|-------------|
| `start-web` | Starts the web interface for the Knowledge Base Agent |
| `start-api` | Starts the API server for programmatic access |
| `start-a2a` | Starts the Agent-to-Agent server for integration with other agents |

## Integration with Other Agents

The Knowledge Base RAG Agent is designed to be easily integrated with other agents through the Agent-to-Agent (A2A) protocol. It can serve as a knowledge retrieval component for more complex agent systems, providing factual company information to support decision-making processes.

## Troubleshooting

If you encounter any issues:

1. Check that your API keys are valid and properly configured
2. Ensure the vector store is properly initialized
3. Verify that the model specified in the .env file is accessible

## License

This project is licensed under a Restricted Use License that allows for educational and research use while prohibiting commercial use without explicit permission. See the [LICENSE](../LICENSE) file for details.

For commercial licensing inquiries, please contact: konrad.jarzyna0@gmail.com
