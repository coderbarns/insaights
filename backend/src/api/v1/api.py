from fastapi import APIRouter

from backend.src.api.v1.endpoints import embeddings

api_router = APIRouter()
api_router.include_router(embeddings.router, prefix="/embeddings", tags=["embeddings"])
