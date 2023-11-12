from typing import List, Optional, Tuple

from selenium import webdriver
from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
import concurrent.futures
import time


def read(url: str) -> Optional[Tuple[str, str]]:
    """
    Renders the page and returns text from paragraphs
    :param url:
    :return: url and content
    """
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")

        driver = Chrome(options=options)
        driver.get(url)

        time.sleep(3)

        body = driver.execute_script("return document.body.innerHTML")
        soup = BeautifulSoup(body, 'html.parser')

        content = ""

        paragraphs = soup.find_all('p')
        for paragraph in paragraphs:
            content += paragraph.get_text() + "\n\n"

        return url, content
    except Exception as ex:
        print(f"Can't read {url}: {ex}")

        return None


def read_many(urls: List[str]) -> dict:
    """
    Reads multiple pages concurrently
    :param urls:
    :return:
    """
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(read, url) for url in urls]

        results = {}
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                results[result[0]] = result[1]

        return results


def test():
    urls = [
        "https://nylcv.org/news/psc-denies-renewable-energy-price-adjustments/",
        "https://www.eia.gov/outlooks/steo/report/electricity.php",
    ]

    for result in read_many(urls):
        print(result)


if __name__ == '__main__':
    test()
