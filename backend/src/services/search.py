from typing import List, Tuple
from sqlalchemy.orm import Session

from src import crud
from src.schemas.search import DocumentSearchResult, QueryResult
from src import db as models


def get_document_search_results(
    db: Session, query_id: int, results: List[Tuple[int, float]]
):
    id_score_mapping = {index + 1: score for index, score in results}
    db_documents = crud.document.get_documents(db=db, ids=list(id_score_mapping))
    crud.document.create_document_query_relationships(db, query_id, id_score_mapping)

    db_documents_mapping = {db_document.id: db_document for db_document in db_documents}
    search_results = []
    for index, score in results:
        db_document = db_documents_mapping[index + 1]
        search_results.append(
            DocumentSearchResult(
                id=db_document.id,
                source=db_document.source,
                text=db_document.text,
                source_type=db_document.source_type,
                link_title=db_document.link_title,
                reliability=db_document.reliability,
                meta=db_document.meta,
                full_text=db_document.full_text,
                score=score,
                impact=0,
            )
        )

    return search_results


def update_document_query_relationship(
    db: Session, query_id: int, params: DocumentSearchResult
):
    crud.document.delete_document_query_relationship(db, params.id, query_id)
    db_relationship = crud.document.create_document_query_relationship(
        db, query_id, params
    )
    db_document = crud.document.update_document_reliability(db, params)
    return DocumentSearchResult(
        id=db_document.id,
        source=db_document.source,
        text=db_document.text,
        source_type=db_document.source_type,
        link_title=db_document.link_title,
        reliability=db_document.reliability,
        meta=db_document.meta,
        full_text=db_document.full_text,
        score=params.score,
        impact=db_relationship.impact,
    )


def get_query(db: Session, query_id: int):
    db_query: models.Query = crud.query.get_query(db, query_id)
    documents = []
    for db_relationship in db_query.document_relationships:
        db_document: models.Document = db_relationship.document
        documents.append(
            DocumentSearchResult(
                id=db_document.id,
                source=db_document.source,
                text=db_document.text,
                source_type=db_document.source_type,
                link_title=db_document.link_title,
                reliability=db_document.reliability,
                meta=db_document.meta,
                full_text=db_document.full_text,
                score=db_relationship.score,
                impact=db_relationship.impact,
            )
        )
    return QueryResult(
        id=db_query.id,
        text=db_query.text,
        documents=documents,
    )
