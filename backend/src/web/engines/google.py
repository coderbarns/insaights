from typing import List

import requests
import json

from src.web.types_ import SearchEngine, SearchResult, SearchEngineCutoff
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

    def set_cutoff(self, value: SearchEngineCutoff):
        cutoffs = {
            SearchEngineCutoff.DAY: "d1",
            SearchEngineCutoff.WEEK: "w1",
            SearchEngineCutoff.MONTH: "m1",
        }

        self._date_restrict = cutoffs[value]

    def search(self, query: str, limit: int = 10) -> List[SearchResult]:
        results = []
        total = 1
        page = 0

        while len(results) < min(total, limit):
            response_results, response_total = self._search_page(query, page)

            results.extend(response_results)
            total = response_total
            page += 1

        return results[:min(total, limit)]

    def _search_page(self, query: str, page: int = 0) -> (List[SearchResult], int):
        """
        Returns results for page and number of total results
        """
        params = {
            "key": KEY,
            "cx": CX,
            "q": query,
            "startIndex": 1 + page * 10,
        }

        if self._date_restrict:
            params["dateRestrict"] = self._date_restrict

        if self._site:
            params["q"] += f" site:{self._site}"

        response = requests.get(URL, params)

        if response.status_code != 200:
            return [], 0

        payload = response.content.decode("utf-8")

        if self._verbose:
            print(payload)

        results = []

        data = json.loads(payload)
        if "items" in data:
            for item in data["items"]:
                url = item["link"]
                title = item["title"]
                description = item["snippet"]
                meta = None

                if "pagemap" in item:
                    meta = item["pagemap"]["metatags"][0]

                result = SearchResult(url, title, description, meta)
                results.append(result)

        total = int(data["searchInformation"]["totalResults"])

        return results, total


def test():
    engine = GoogleEngine("m1", verbose=True, site="bbc.com")
    results = engine.search("stainless steel manufacturing", 15)

    print("COUNT:", len(results))

    for result in results:
        print(result)


if __name__ == "__main__":
    test()
