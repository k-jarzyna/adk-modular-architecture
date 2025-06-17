from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class ServerConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")
    mcp_port: int = Field(default=8000)
    firecrawl_api_key: str = Field()
    transport: str = Field(default="sse")