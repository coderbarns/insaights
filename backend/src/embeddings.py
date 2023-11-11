import txtai

import src.db as models
import src.schemas.document as schemas
from src.deps import get_settings

settings = get_settings()
_embeddings = txtai.Embeddings()

if _embeddings.exists():
    _embeddings.load(settings.EMBEDDINGS_PATH)


def get_embeddings():
    return _embeddings


def upsert(db_documents: list[models.Document]):
    documents = [schemas.Document(db_document.id, db_document.text) for db_document in db_documents]
    _embeddings.upsert(documents)
    _embeddings.save(settings.EMBEDDINGS_PATH)


def search(db_documents: list[models.Document]):
    documents = [schemas.Document(db_document.id, db_document.text) for db_document in db_documents]
    _embeddings.upsert(documents)
    _embeddings.save(settings.EMBEDDINGS_PATH)
