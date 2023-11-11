from sqlalchemy.orm import Session

from src.crud.document import get_documents
from src.schemas.document import DocumentSearchResult


def get_document_search_results(db: Session, results: list[tuple[int, float]]):
    ids = [id for id, _ in results]
    db_documents = get_documents(db=db, ids=ids)
    db_documents_mapping = {db_document.id: db_document for db_document in db_documents}

    search_results = []
    for id, score in results:
        db_document = db_documents_mapping[id]
        search_results.append(
            DocumentSearchResult(
                id=db_document.id,
                source=db_document.source,
                text=db_document.text,
                source_type=db_document.source_type,
                link_title=db_document.link_title,
                reliable=db_document.reliable,
                score=score,
            )
        )

    return search_results