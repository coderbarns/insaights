from typing import NamedTuple, List, Union


class SearchResult(NamedTuple):
    url: str
    title: str
    snippet: Union[str, None]
    description: Union[str, None]


class SearchEngine:
    def search(self, query: str) -> List[SearchResult]:
        pass

