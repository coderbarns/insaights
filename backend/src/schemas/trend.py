from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class BaseTrend(BaseModel):
    title: str
    description: str
    keywords: List[str]
    urls: Optional[List[str]]
    scrape_interval: str
    summary: str
    updated: str


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
                "summary": "example summary",
                "updated": datetime.now().isoformat()
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
                "summary": "summary",
                "updated": datetime.now().isoformat()
            }
        }
