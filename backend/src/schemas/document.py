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
    reliability: Optional[float]


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
