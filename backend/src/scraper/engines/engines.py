from src.scraper.engines.google import GoogleEngine
from src.scraper.types_ import SearchEngine
from src.scraper.engines.yle import YleEngine

# define custom search engines for sites here
engines = {
    "yle.fi": YleEngine,
}


def get(site: str) -> SearchEngine:
    if site in engines:
        return engines[site]()

    return GoogleEngine(site=site)
