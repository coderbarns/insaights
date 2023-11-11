from functools import lru_cache
from src.config import Settings
from src.db import SessionLocal
import txtai

embeddings = None

@lru_cache
def get_settings():
    return Settings()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_embeddings():
    global embeddings
    settings = get_settings()
    embeddings = txtai.Embeddings(config=settings.TXTAI_CONFIG)
    return embeddings
