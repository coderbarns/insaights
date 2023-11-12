from pydantic import BaseModel
from typing import Optional

from .document import Document
from .query import Query


class DocumentSearchResult(Document):
    score: float
    impact: Optional[float]


class DocumentSearchResponse(BaseModel):
    query: Query
    summary: str
    documents: list[DocumentSearchResult]


class DocumentSearchRequest(BaseModel):
    query: str

    class Config:
        schema_extra = {
            "example": {
                "texts": ["How much does steel manufacturing rock?"],
            }
        }


class DocumentQueryUpdateRequest(DocumentSearchResult):
    class Config:
        schema_extra = {
            "example": {
                "reliability": 0.5,
                "impact": -0.5,
            }
        }


class QueryResult(Query):
    documents: list[DocumentSearchResult]
