from typing import List

import logging

from src.conversation.assistant import Assistant
from src.crud.document import create_documents
from src.crud.trend import update_trend, create_trend
from src.deps import get_db
from src.services import embeddings
from src.services.search import get_document_search_results
from src.web.summarizer import UrlSummarizer
from src.web.engines import engines
from src.web.engines.google import GoogleEngine
from src import db as models
from src.web.types_ import SearchEngineCutoff


def fetch_trend(trend: models.Trend):
    logging.debug(f"fetching trend {trend}")

    db = next(get_db())

    documents = get_documents(trend)
    db_documents = create_documents(db, documents)
    embeddings.upsert(db_documents)

    results = embeddings.search(query=trend.description, limit=10)
    documents_for_summary = get_document_search_results(db, results)

    logging.debug("fetching summary")

    assistant = Assistant()
    conversation = assistant.start(trend.description, documents_for_summary)
    trend.summary = conversation[-1].content

    update_trend(db, trend.id, trend)


def get_documents(trend: models.Trend) -> List[models.Document]:
    results = []

    cutoff = SearchEngineCutoff.from_value(trend.scrape_interval)
    keyword_str = " ".join(trend.keywords)

    if trend.urls:
        for url in trend.urls:
            engine = engines.get(url)
            engine.set_cutoff(cutoff)
            results.extend(engine.search(keyword_str))

    # default search from all
    google = GoogleEngine(cutoff)
    results.extend(google.search(keyword_str))

    documents = []
    for result in results:
        logging.debug(f"processing result {result.title}")

        try:
            summarizer = UrlSummarizer(result.url)
            short_summary = summarizer.make(3)

            if not short_summary:
                continue  # skip empty document

            document = models.Document()
            document.text = result.description + " " + short_summary  # add snippet and summary for embeddings
            document.source_type = "url"
            document.source = "url"
            document.link_title = result.title
            document.meta = result.meta
            document.full_text = summarizer.make(25)

            documents.append(document)
        except Exception as ex:
            logging.warning(f"Can't summarize {result.url}: {ex}")

            continue

    return documents


def test():
    trend = models.Trend()
    trend.title = "test"
    trend.description = "How..."
    trend.keywords = ["energy price forecast"]
    trend.urls = ["cnn.com", "yle.fi"]
    trend.scrape_interval = "monthly"
    trend.summary = "Pending"

    db = next(get_db())
    trend = create_trend(db, trend)

    fetch_trend(trend)


if __name__ == '__main__':
    test()
