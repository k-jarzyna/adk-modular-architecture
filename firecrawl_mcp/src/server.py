from dotenv import load_dotenv
from src.infrastructure.config import ServerConfig
from src.infrastructure.mcp_instance import mcp
import src.tool.scrape_url

load_dotenv()

config = ServerConfig()

if __name__ == '__main__':
    mcp.run(transport=config.transport, port=config.mcp_port)