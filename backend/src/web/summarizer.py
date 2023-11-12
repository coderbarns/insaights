from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


def init_nltk():
    """
    Run to download NLTK
    """
    import nltk
    nltk.download()


class UrlSummarizer:
    def __init__(self, url: str, language: str = "english"):
        self._url = url
        self._language = language

        # see https://github.com/miso-belica/sumy
        self._parser = HtmlParser.from_url(self._url, Tokenizer(self._language))
        # parser = PlaintextParser.from_string("Check this out.", Tokenizer(LANGUAGE))
        self._stemmer = Stemmer(self._language)
        self._summarizer = Summarizer(self._stemmer)
        self._summarizer.stop_words = get_stop_words(self._language)

    def make(self, sentences: int = 5) -> str:
        sentences = self._summarizer(self._parser.document, sentences)

        return " ".join([str(sentence) for sentence in sentences])


def test():
    url = "https://yle.fi/a/74-20011270"

    summarizer = UrlSummarizer(url)

    print(summarizer.make())


if __name__ == "__main__":
    test()
