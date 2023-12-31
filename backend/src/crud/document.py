from sqlalchemy import select
from sqlalchemy.orm import Session
from typing import List, Dict

from src import schemas
from src import db as models


def create_documents(
    db: Session, documents: List[models.Document]
) -> List[models.Document]:
    db.bulk_save_objects(documents)
    db.commit()
    return documents


def create_input_documents(
    db: Session, documents: List[schemas.document.InsertDocument]
) -> List[models.Document]:
    db_documents = [
        models.Document(
            text=document.text, source=document.source, source_type="insert"
        )
        for document in documents
    ]
    db.bulk_save_objects(db_documents)
    db.commit()
    return db_documents


def update_document_reliability(
    db: Session, params: schemas.search.DocumentSearchResult
):
    document: models.Document = db.execute(
        select(models.Document).where(models.Document.id == params.id)
    ).first()[0]
    document.reliability = params.reliability
    db.flush()
    return document


def get_documents(db: Session, ids: List[int]) -> List[models.Document]:
    return db.query(models.Document).filter(models.Document.id.in_(ids)).all()


def create_document_query_relationships(
    db: Session, query_id: int, id_score_mapping: Dict[int, float]
):
    db_document_query_relationships = [
        models.DocumentQuery(
            document_id=id,
            query_id=query_id,
            impact=0,
            score=score,
        )
        for id, score in id_score_mapping.items()
    ]
    db.bulk_save_objects(db_document_query_relationships)
    db.commit()


def update_document_query_relationship(
    db: Session, query_id: int, params: schemas.search.DocumentSearchResult
):
    db.query(models.DocumentQuery).filter(
        models.DocumentQuery.query_id == query_id,
        models.DocumentQuery.document_id == params.id,
    ).update(
        {
            models.DocumentQuery.impact: params.impact,
            models.DocumentQuery.score: params.score,
        }
    )
    db.commit()
    return params
