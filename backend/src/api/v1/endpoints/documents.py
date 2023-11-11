from fastapi import APIRouter, Depends
from txtai import Embeddings

from src.deps import get_embeddings
from backend.src.schemas.document import (
    CreateDocumentsRequest,
    CreateDocumentsResponse,
    SearchRequest,
    SearchResponse,
)

router = APIRouter()


@router.post("/")
async def create_document(
    params: CreateDocumentsRequest, embeddings: Embeddings = Depends(get_embeddings)
) -> CreateDocumentsResponse:
    embeddings.index(params.documents)
    embeddings.save("elastic")
    return CreateDocumentsResponse(message="Stored!")


@router.post("/search/")
async def search(
    params: SearchRequest, embeddings: Embeddings = Depends(get_embeddings)
) -> SearchResponse:
    embeddings.load("elastic")
    results = embeddings.search(query=params.query, limit=2)
    return SearchResponse(results=results)
