from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    Float,
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
    text = Column(String)
    source_type = Column(String)
    source = Column(String)
    link_title = Column(String, nullable=True)
    reliable = Column(Float, nullable=True)


class Prompt(Base):
    __tablename__ = "prompts"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)


class DocumentPrompt(Base):
    __tablename__ = "documents__prompts"

    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, ForeignKey("documents.id"))
    prompt_id = Column(Integer, ForeignKey("prompts.id"))
    relevance = Column(Float)
    impact = Column(Float)

    prompt = relationship("Prompt", backref="document_relationships")
    document = relationship("Document", backref="prompt_relationships")


class DocumentTrend(Base):
    __tablename__ = "documents__trends"

    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, ForeignKey("documents.id"))
    trend_id = Column(Integer, ForeignKey("trends.id"))
    relevance = Column(Float)
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


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
