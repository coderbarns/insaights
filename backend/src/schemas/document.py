from pydantic import BaseModel
from typing import Optional


class BaseDocument(BaseModel):
    source: str
    text: str


class InsertDocument(BaseDocument):
    pass


class InputLinkDocument(BaseDocument):
    source_type: str
    link_title: Optional[str]


class Document(BaseDocument):
    id: int
    source_type: str
    link_title: Optional[str]
    reliable: Optional[float]


class DocumentSearchResult(Document):
    score: float


class CreateDocumentsRequest(BaseModel):
    source: str
    texts: list[str]

    class Config:
        schema_extra = {
            "example": {
                "texts": ["Steel manufacturing rocks!"],
            }
        }


class CreateDocumentsResponse(BaseModel):
    message: str


class DocumentSearchRequest(BaseModel):
    query: str

    class Config:
        schema_extra = {
            "example": {
                "texts": ["How much does steel manufacturing rock?"],
            }
        }


class DocumentSearchResponse(BaseModel):
    summary: str
    documents: list[DocumentSearchResult]
