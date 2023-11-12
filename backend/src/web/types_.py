from __future__ import annotations

from enum import Enum
from typing import NamedTuple, List, Optional


class SearchResult(NamedTuple):
    url: str
    title: str
    description: str
    meta: Optional[dict]
    # TODO: add assets/images


class SearchEngineCutoff(Enum):
    """
    Trend.scrape_interval values
    """
    DAY = "daily"
    WEEK = "weekly"
    MONTH = "monthly"

    @staticmethod
    def from_value(value: str) -> Optional[SearchEngineCutoff]:
        for cutoff in SearchEngineCutoff:
            if cutoff.value.lower() == value.lower():
                return cutoff
        return None


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
