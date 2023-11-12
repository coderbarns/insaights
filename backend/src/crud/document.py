from typing import List

from sqlalchemy.orm import Session

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


def get_documents(db: Session, ids: List[int]) -> List[models.Document]:
    return db.query(models.Document).filter(models.Document.id.in_(ids)).all()
