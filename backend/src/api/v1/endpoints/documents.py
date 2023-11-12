from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.crud.document import create_input_documents
from src.crud.query import create_query
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
    create_query(db, params.query)
    results = embeddings.search(query=params.query, limit=20)
    document_search_results = get_document_search_results(db, results)
    return schemas.DocumentSearchResponse(
        summary="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
        documents=document_search_results,
    )
