from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    Float,
    JSON,
    DateTime,
    create_engine,
)
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

from src.config import settings

engine = create_engine(settings.get_pg_connection_uri())
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)  # short summary for embeddings (5 sentences)
    source_type = Column(String)  # url vs other reference
    source = Column(String)  # url
    link_title = Column(String, nullable=True)
    reliability = Column(Float, nullable=True)
    meta = Column(JSON, nullable=True)  # content from meta tags
    full_text = Column(String, nullable=True)


class DocumentTrend(Base):
    __tablename__ = "documents__trends"

    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, ForeignKey("documents.id"))
    trend_id = Column(Integer, ForeignKey("trends.id"))
    impact = Column(Float)

    trend = relationship("Trend", backref="document_relationships")
    document = relationship("Document", backref="trend_relationships")


class Trend(Base):
    __tablename__ = "trends"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    keywords = Column(ARRAY(String))
    urls = Column(ARRAY(String), nullable=True)
    scrape_interval = Column(String)
    summary = Column(String)
    updated = Column(DateTime)


class Query(Base):
    __tablename__ = "queries"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)


class DocumentQuery(Base):
    __tablename__ = "documents__queries"

    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, ForeignKey("documents.id"))
    query_id = Column(Integer, ForeignKey("queries.id"))
    impact = Column(Float)
    score = Column(Float)

    document = relationship("Document", backref="query_relationships")
    query = relationship("Query", backref="document_relationships")


if __name__ == "__main__":
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
