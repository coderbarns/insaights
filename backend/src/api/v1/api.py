from fastapi import APIRouter

from backend.src.api.v1.endpoints import documents

api_router = APIRouter()
api_router.include_router(documents.router, prefix="/documents", tags=["documents"])
