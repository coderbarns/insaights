from pydantic import BaseModel
from typing import Optional, List


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
    meta: Optional[dict]
    full_text: Optional[str]


class CreateDocumentsRequest(BaseModel):
    source: str
    texts: List[str]

    class Config:
        schema_extra = {
            "example": {
                "texts": ["Steel manufacturing rocks!"],
            }
        }


class CreateDocumentsResponse(BaseModel):
    message: str
