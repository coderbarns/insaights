from typing import NamedTuple, List, Union


class SearchResult(NamedTuple):
    url: str
    title: str
    description: str
    meta: Union[dict, None]


class SearchEngine:
    def search(self, query: str, limit: int = 10) -> List[SearchResult]:
        pass

