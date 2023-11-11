from sqlalchemy.orm import Session

from src import db as models


def create_query(db: Session, text: str) -> models.Query:
    db_query = models.Query(text=text)
    db.add(db_query)
    db.commit()
    db.refresh(db_query)
    return db_query
