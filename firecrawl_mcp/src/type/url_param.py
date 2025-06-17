from pydantic import BaseModel, HttpUrl, Field

class UrlParam(BaseModel):
    url: HttpUrl = Field()