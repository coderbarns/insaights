from sqlalchemy.orm import Session, selectinload

from src import db as models


def get_queries(db: Session) -> models.Query:
    return db.query(models.Query).all()


def create_query(db: Session, text: str) -> models.Query:
    db_query = models.Query(text=text)
    db.add(db_query)
    db.commit()
    db.refresh(db_query)
    return db_query


def get_query(db: Session, query_id: int) -> models.Query:
    return (
        db.query(models.Query)
        .filter(models.Query.id == query_id)
        .options(
            selectinload(models.Query.document_relationships).selectinload(models.DocumentQuery.document)
        )
        .first()
    )
