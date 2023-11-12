from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from src.deps import get_db
from src import schemas
from src.services import search
from src.crud import query as crud

router = APIRouter()


@router.get("/")
async def get_queries(
    db: Session = Depends(get_db),
) -> List[schemas.query.Query]:
    return crud.get_queries(db)


@router.get("/{query_id}/")
async def get_query(
    query_id: int,
    db: Session = Depends(get_db),
) -> schemas.search.QueryResult:
    return search.get_query(db, query_id)


@router.put("/{query_id}/documents/{document_id}/")
async def update_document_query_relationship(
    query_id: int,
    document_id: int,
    params: schemas.search.DocumentSearchResult,
    db: Session = Depends(get_db),
) -> schemas.search.DocumentSearchResult:
    return search.update_document_query_relationship(db, query_id, params)
