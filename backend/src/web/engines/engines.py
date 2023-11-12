from src.web.engines.google import GoogleEngine
from src.web.types_ import SearchEngine
from src.web.engines.yle import YleEngine

# define custom search engines for sites here
engines = {
    "yle.fi": YleEngine,
}


def get(site: str) -> SearchEngine:
    if site in engines:
        return engines[site]()

    return GoogleEngine(site=site)
