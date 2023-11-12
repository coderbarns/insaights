from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.deps import get_db
from src.schemas import trend as schemas
from src.crud import trend as crud
from src.services.worker import update_trend_queue

router = APIRouter()


@router.get("/", response_model=List[schemas.Trend])
async def get_trends(
    db: Session = Depends(get_db),
):
    return crud.get_trends(db)


@router.post("/", response_model=schemas.Trend)
async def create_trend(
    params: schemas.CreateTrendRequest,
    db: Session = Depends(get_db),
):
    db_trend = crud.create_trend(db, params)

    update_trend_queue.put(db_trend)

    return db_trend


@router.put("/{trend_id}/", response_model=schemas.Trend)
async def update_trend(
    trend_id: int,
    params: schemas.UpdateTrendRequest,
    db: Session = Depends(get_db),
):
    db_trend = crud.update_trend(db, trend_id, params)

    update_trend_queue.put(db_trend)

    return db_trend


@router.delete("/{trend_id}/", status_code=204)
async def delete_trend(
    trend_id: int,
    db: Session = Depends(get_db),
):
    return crud.delete_trend(db, trend_id)
