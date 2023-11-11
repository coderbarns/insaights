from sqlalchemy.orm import Session

from src.schemas import document as schemas
from src import db as models


def create_input_documents(
    db: Session, documents: list[schemas.InsertDocument]
) -> list[models.Document]:
    db_documents = [
        models.Document(
            text=document.text, source=document.source, source_type="insert"
        )
        for document in documents
    ]
    db.bulk_save_objects(db_documents)
    db.commit()
    return db_documents


def get_documents(db: Session, ids: list[int]) -> list[models.Document]:
    return db.query(models.Document).filter(models.Document.id.in_(ids)).all()
