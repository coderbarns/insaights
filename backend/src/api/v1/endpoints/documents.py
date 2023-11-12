from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.conversation.assistant import get_assistant
from src.crud.document import create_input_documents
from src.crud.query import create_query
from src.deps import get_db
from src import schemas
from src.services import embeddings
from src.services.search import get_document_search_results

router = APIRouter()


@router.post("/")
async def create_document(
    params: schemas.document.CreateDocumentsRequest,
    db: Session = Depends(get_db),
) -> schemas.document.CreateDocumentsResponse:
    documents = [
        schemas.document.InsertDocument(source=params.source, text=text)
        for text in params.texts
    ]
    db_documents = create_input_documents(db, documents)
    embeddings.upsert(db_documents)
    return schemas.document.CreateDocumentsResponse(message="Stored!")


@router.post("/search/")
async def search(
    params: schemas.search.DocumentSearchRequest,
    db: Session = Depends(get_db),
) -> schemas.search.DocumentSearchResponse:
    db_query = create_query(db, params.query)
    query = schemas.query.Query(id=db_query.id, text=db_query.text)

    assistant = get_assistant(params.conversation_id)
    if len(assistant.get_messages()) > 1:
        # continue conversation
        assistant.run(params.query)
    else:
        # start conversation
        embeddings.load()
        results = embeddings.search(query=params.query, limit=5)
        document_search_results = get_document_search_results(db, results, query.id)
        assistant.start(params.query, document_search_results)

    return schemas.search.DocumentSearchResponse(
        # query=query,
        messages=assistant.get_messages(),
        documents=assistant.get_documents(),
    )
