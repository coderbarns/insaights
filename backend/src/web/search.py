from typing import List

from src.web.summarizer import UrlSummarizer
from src.web.engines import engines
from src.web.engines.google import GoogleEngine
from src import db as models
from src.web.types_ import SearchEngineCutoff


def get_documents(trend: models.Trend) -> List[models.Document]:
    results = []

    cutoff = SearchEngineCutoff.from_value(trend.scrape_interval)

    if trend.urls:
        for url in trend.urls:
            engine = engines.get(url)
            engine.set_cutoff(cutoff)
            results.extend(engine.search(" ".join(trend.keywords)))

    # default search from all
    google = GoogleEngine(cutoff)
    results.extend(google.search(trend.keywords))

    documents = []
    for result in results:
        try:
            summarizer = UrlSummarizer(result.url)
            short_summary = summarizer.make()

            if not short_summary:
                continue  # skip empty document

            document = models.Document()
            document.text = result.description + " " + short_summary  # add snippet and summary for embeddings
            document.source_type = "url"
            document.source = "url"
            document.link_title = result.title
            document.meta = result.meta
            document.full_text = summarizer.make(1000)

            documents.append(document)
        except Exception as ex:
            print(f"Can't summarize {result.url}: {ex}")

            continue

    return documents


def test():
    trend = models.Trend()
    trend.keywords = ["energy price forecast"]
    trend.urls = ["cnn.com", "yle.fi"]
    trend.scrape_interval = "monthly"

    for document in get_documents(trend):
        print(document)


if __name__ == '__main__':
    test()
