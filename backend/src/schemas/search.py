from pydantic import BaseModel


class IndexRequest(BaseModel):
    text: str

    class Config:
        schema_extra = {
            "example": {
                "text": "Steel manufacturing rocks!",
            }
        }


class IndexResponse(BaseModel):
    message: str
