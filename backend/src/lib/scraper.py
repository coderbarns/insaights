from typing import List

from src.lib.engines import engines


def scrape(query: str, description: str, sites: List["str"]):
    results = []

    for site in sites:
        engine = engines.get(site)

        for result in engine.search(query):
            results.append(result)

    print(results)
