from src.lib.engines.google import GoogleEngine
from src.lib.engines._types import SearchEngine
from src.lib.engines.yle import YleEngine

# define custom search engines for sites here
engines = {
    "yle.fi": YleEngine,
}


def get(site: str) -> SearchEngine:
    if site in engines:
        return engines[site]()

    return GoogleEngine(site=site)
