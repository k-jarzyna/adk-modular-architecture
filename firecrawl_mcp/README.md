# FireCrawl MCP

A web scraping microservice built with MCP that provides a tool to scrape web pages and return their content in Markdown format.

## Overview

FireCrawl MCP is a lightweight service that integrates the FireCrawl web scraping library with the MCP framework, enabling easy integration with AI agents and other services that need web content extraction capabilities.

## Available Tools

| Tool | Description |
|------|-------------|
| `scrape_url` | Scrapes content from a specified URL and returns it as Markdown |

## Development Setup

### Prerequisites

- Python 3.13+
- Poetry (for dependency management)
- FireCrawl API key ([FireCrawl website](https://firecrawl.dev))

### Environment Setup

1. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

2. Create a `.env` file by copying the example:
   ```bash
   cp .env.example .env
   ```

3. Edit the `.env` file and add your FireCrawl API key:
   ```
   FIRECRAWL_API_KEY=your_api_key_here
   MCP_PORT=5000  # Optional: Change the port if needed
   ```

### Running the Service

You can start the service using the provided CLI command:

```bash
poetry run start-mcp
```

This will start the MCP server on the port specified in your `.env` file (default: 5000).

## Available CLI Commands

| Command | Description |
|---------|-------------|
| `start-mcp` | Starts the FireCrawl MCP service |

## Integration with AI Agents

FireCrawl MCP is designed to be easily integrated with AI agent frameworks. It can be used to provide web scraping capabilities to agents that need to access and process web content.

## Troubleshooting

If you encounter any issues:

1. Check that your FireCrawl API key is valid
2. Ensure the target URL is accessible and contains content that can be scraped
3. Check the error message returned in the `error` field of the response

## License

This project is licensed under a Restricted Use License that allows for educational and research use while prohibiting commercial use without explicit permission. See the [LICENSE](../LICENSE) file for details.

For commercial licensing inquiries, please contact: konrad.jarzyna0@gmail.com
