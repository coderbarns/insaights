from functools import lru_cache
from src.config import Settings
from src.db import SessionLocal


@lru_cache
def get_settings():
    return Settings()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
