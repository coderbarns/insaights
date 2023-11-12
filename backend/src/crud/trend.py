from datetime import datetime
from typing import List

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.schemas import trend as schemas
from src import db as models


def get_trends(db: Session) -> List[models.Trend]:
    return db.query(models.Trend).all()


def create_trend(db: Session, trend: schemas.Trend) -> models.Trend:
    db_trend = models.Trend(
        title=trend.title,
        description=trend.description,
        keywords=trend.keywords,
        urls=trend.urls,
        scrape_interval=trend.scrape_interval,
        summary=trend.summary,
        updated=datetime.now().isoformat(),
    )
    db.add(db_trend)
    db.commit()
    db.refresh(db_trend)
    return db_trend


def update_trend(db: Session, id: int, trend: schemas.Trend) -> models.Trend:
    db_trend: models.Trend = db.execute(select(models.Trend).where(models.Trend.id==id)).first()[0]
    db_trend.title=trend.title
    db_trend.description=trend.description
    db_trend.keywords=trend.keywords
    db_trend.urls=trend.urls
    db_trend.scrape_interval=trend.scrape_interval
    db_trend.summary=trend.summary
    db_trend.updated=datetime.now().isoformat()
    db.flush()
    return db_trend


def delete_trend(db: Session, id: int) -> None:
    db.query(models.Trend).filter(models.Trend.id==id).delete()
    db.commit()
