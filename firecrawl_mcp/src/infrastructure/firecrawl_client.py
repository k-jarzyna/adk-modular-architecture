from firecrawl import FirecrawlApp

from src.infrastructure.config import ServerConfig

class FireCrawlClient:
    _instance = None
    _client: FirecrawlApp = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FireCrawlClient, cls).__new__(cls)
            cls._instance._initialize_client()
        return cls._instance

    def _initialize_client(self) -> None:
        config = ServerConfig()
        self._client = FirecrawlApp(api_key=config.firecrawl_api_key)

    @staticmethod
    def get_client() -> FirecrawlApp:
        instance = FireCrawlClient()
        return instance._client