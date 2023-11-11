from pydantic import BaseModel
from typing import Optional


class BaseDocument(BaseModel):
    source: str
    text: str


class InputDocument(BaseDocument):
    pass


class InputLinkDocument(BaseDocument):
    source_type: str
    link_title: Optional[str]


class Document(BaseDocument):
    id: int
    source_type: str
    link_title: Optional[str]
    reliable: Optional[float]


class CreateDocumentsRequest(BaseModel):
    documents: list[BaseDocument]

    class Config:
        schema_extra = {
            "example": {
                "texts": ["Steel manufacturing rocks!"],
            }
        }


class CreateDocumentsResponse(BaseModel):
    message: str


class SearchRequest(BaseModel):
    query: str

    class Config:
        schema_extra = {
            "example": {
                "texts": ["How much does steel manufacturing rock?"],
            }
        }


class SearchResponse(BaseModel):
    results: list[tuple[float, str]]
