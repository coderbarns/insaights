from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from txtai import Embeddings

from src.config import Settings
from src.api.deps import get_db, get_embeddings, get_settings
from src.schemas.search import IndexRequest, IndexResponse

router = APIRouter()


@router.post("/index/")
async def search(params: IndexRequest, embeddings: Embeddings = Depends(get_embeddings), settings: Settings = Depends(get_settings)) -> IndexResponse:
    print("Indexing...")
    embeddings.upsert([params.text])
    print("Done.")
    embeddings.save("vectors")
    return IndexResponse(message="Stored!")
