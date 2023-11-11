from typing import List

import requests
import json

from src.lib.engines.types_ import SearchEngine, SearchResult
from src.config import settings

URL = "https://www.googleapis.com/customsearch/v1"
KEY = settings.GOOGLE_KEY
CX = settings.GOOGLE_CX


class GoogleEngine(SearchEngine):
    """
    https://developers.google.com/custom-search/v1/reference/rest/v1/cse/list#request
    """
    def __init__(self, date_restrict: str = None, site: str = None, verbose: bool = False):
        self._date_restrict = date_restrict
        self._site = site
        self._verbose = verbose

    def search(self, query: str) -> List[SearchResult]:
        params = {
            "key": KEY,
            "cx": CX,
            "q": query,
            # "startIndex": 1 + page * 10,
        }

        if self._date_restrict:
            params["dateRestrict"] = self._date_restrict

        if self._site:
            params["q"] += f" site:{self._site}"

        response = requests.get(URL, params)

        if response.status_code != 200:
            return []

        payload = response.content.decode("utf-8")

        if self._verbose:
            print(payload)

        results = []

        data = json.loads(payload)
        for item in data["items"]:
            url = item["link"]
            title = item["title"]
            snippet = item["snippet"]
            description = None

            if "og:description" in item["pagemap"]["metatags"][0]:
                description = item["pagemap"]["metatags"][0]["og:description"]

            result = SearchResult(url, title, snippet, description)
            results.append(result)

        return results


def test():
    engine = GoogleEngine("m1", verbose=True)
    results = engine.search("energy price development news")
    for result in results:
        print(result)


if __name__ == "__main__":
    test()
