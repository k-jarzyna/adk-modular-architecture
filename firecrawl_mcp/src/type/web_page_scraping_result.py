from typing import Union

from pydantic import BaseModel, Field


class WebPageScrapingResult(BaseModel):
    url: str = Field()
    markdown: Union[str, None] = Field(default=None)
    success: bool = Field(default=True)
    error: Union[str, None] = Field(default=None)