from fastapi import APIRouter

from src.api.v1.endpoints import documents, trends

api_router = APIRouter()
api_router.include_router(documents.router, prefix="/documents", tags=["documents"])
api_router.include_router(trends.router, prefix="/trends", tags=["trends"])
