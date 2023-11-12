from typing import List

import txtai

import src.db as models
from src.deps import get_settings

settings = get_settings()
_embeddings = txtai.Embeddings()

if _embeddings.exists():
    _embeddings.load(settings.EMBEDDINGS_PATH)


def get_embeddings():
    return _embeddings


def upsert(db_documents: List[models.Document]):
    documents = [(db_document.id, db_document.text) for db_document in db_documents]
    try:
        _embeddings.upsert(documents)
    except AttributeError:
        _embeddings.index(documents)
    _embeddings.save(settings.EMBEDDINGS_PATH)


def search(query: str, limit: int = 3):
    return _embeddings.search(query, limit=limit)
