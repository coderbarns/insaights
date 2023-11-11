from enum import Enum
from typing import NamedTuple, List, Optional


class SearchResult(NamedTuple):
    url: str
    title: str
    description: str
    meta: Optional[dict]


class SearchEngineCutoff(Enum):
    DAY = 1
    WEEK = 2
    MONTH = 3


class SearchEngine:
    def set_cutoff(self, value: SearchEngineCutoff):
        pass

    def search(self, query: str, limit: int = 10) -> List[SearchResult]:
        pass


class Trend(NamedTuple):
    title: str
    keywords: str
    description: str
    sites: List[str]  # domains
    interval: SearchEngineCutoff
