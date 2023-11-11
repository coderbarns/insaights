from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.deps import get_db
from src.schemas.document import (
    CreateDocumentsRequest,
    CreateDocumentsResponse,
    InsertDocument,
    SearchRequest,
    SearchResponse,
)
from src.crud.document import create_input_documents
from src import embeddings

router = APIRouter()


@router.post("/")
async def create_document(
    params: CreateDocumentsRequest,
    db: Session = Depends(get_db),
) -> CreateDocumentsResponse:
    documents = [InsertDocument(source=params.source, text=text) for text in params.texts]
    db_documents = create_input_documents(db, documents)
    embeddings.upsert(db_documents)
    return CreateDocumentsResponse(message="Stored!")


@router.post("/search/")
async def search(params: SearchRequest) -> SearchResponse:
    results = embeddings.search(query=params.query, limit=2)
    return SearchResponse(results=results)
