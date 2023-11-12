from pydantic import BaseModel
from typing import List, Optional

from .document import Document
from .query import Query


class DocumentSearchResult(Document):
    score: float
    impact: Optional[float]


class DocumentSearchResponse(BaseModel):
    query: Query
    messages: List
    documents: List


class DocumentSearchRequest(BaseModel):
    conversation_id: str
    query: str

    class Config:
        schema_extra = {
            "example": {
                "conversation_id": 1,
                "query": ["How much does steel manufacturing rock?"],
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
    documents: List[DocumentSearchResult]
