from pydantic import BaseModel
from typing import Optional


class BaseTrend(BaseModel):
    title: str
    description: str
    keywords: list[str]
    urls: Optional[list[str]]
    scrape_interval: str


class CreateTrend(BaseTrend):
    pass


class Trend(BaseTrend):
    id: int


class CreateTrendRequest(CreateTrend):
    class Config:
        schema_extra = {
            "example": {
                "title": "My trend",
                "description": "My description",
                "keywords": ["keyword1", "keyword2"],
                "urls": ["google.com", "twitter.com"],
                "scrape_interval": ["daily"],
            }
        }


class UpdateTrendRequest(BaseTrend):
    id: int

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "My trend",
                "description": "My description",
                "keywords": ["keyword1", "keyword2"],
                "urls": ["google.com", "twitter.com"],
                "scrape_interval": ["daily"],
            }
        }