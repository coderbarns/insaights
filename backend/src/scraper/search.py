from typing import List

from src.scraper.types_ import Trend, SearchEngineCutoff, SearchResult
from src.scraper.engines import engines
from src.scraper.engines.google import GoogleEngine


def get_results(trend: Trend) -> List[SearchResult]:
    results = []

    for site in trend.sites:
        engine = engines.get(site)
        engine.set_cutoff(trend.interval)
        results.extend(engine.search(trend.keywords))

    google = GoogleEngine("m1")
    results.extend(google.search(trend.keywords))

    return results


def test():
    trend = Trend("",
                  "car price forecast",
                  "",
                  ["cnn.com", "yle.fi", "ft.com"],
                  SearchEngineCutoff.MONTH)

    for result in get_results(trend):
        print(result)


if __name__ == '__main__':
    test()
