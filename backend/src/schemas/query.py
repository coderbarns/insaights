from pydantic import BaseModel


class BaseQuery(BaseModel):
    text: str


class CreateQuery(BaseQuery):
    pass


class Query(BaseQuery):
    id: int
