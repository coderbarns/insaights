from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.crud.document import create_input_documents
from src.deps import get_db
from src.schemas import document as schemas
from src.services import embeddings
from src.services.search import get_document_search_results

router = APIRouter()


@router.post("/")
async def create_document(
    params: schemas.CreateDocumentsRequest,
    db: Session = Depends(get_db),
) -> schemas.CreateDocumentsResponse:
    documents = [
        schemas.InsertDocument(source=params.source, text=text) for text in params.texts
    ]
    db_documents = create_input_documents(db, documents)
    embeddings.upsert(db_documents)
    return schemas.CreateDocumentsResponse(message="Stored!")


@router.post("/search/")
async def search(
    params: schemas.DocumentSearchRequest,
    db: Session = Depends(get_db),
) -> schemas.DocumentSearchResponse:
    results = embeddings.search(query=params.query, limit=2)
    document_search_results = get_document_search_results(db, results)
    return schemas.DocumentSearchResponse(results=document_search_results)
