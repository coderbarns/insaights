from typing import List

import requests
import json

from src.lib.engines.types_ import SearchEngine, SearchResult
from src.config import settings

URL = "https://yle-fi-search.api.yle.fi/v1/search"
APP_ID = "hakuylefi_v2_prod"
APP_KEY = settings.YLE_APP_KEY


class YleEngine(SearchEngine):
    def __init__(self, language: str = "en", verbose: bool = False):
        self._language = language
        self._verbose = verbose

    def search(self, query: str) -> List[SearchResult]:
        params = {
            "app_id": APP_ID,
            "app_key": APP_KEY,
            "language": self._language,
            "query": query,
        }

        response = requests.get(URL, params)

        if response.status_code != 200:
            return []

        payload = response.content.decode("utf-8")

        if self._verbose:
            print(payload)

        results = []

        data = json.loads(payload)
        for item in data["data"]:
            url = item["url"]["full"]
            title = item["headline"]
            snippet = None
            description = item["lead"]

            result = SearchResult(url, title, snippet, description)
            results.append(result)

        return results


def test():
    yle = YleEngine(verbose=True)
    results = yle.search("energia hinta")
    for result in results:
        print(result)


if __name__ == "__main__":
    test()
