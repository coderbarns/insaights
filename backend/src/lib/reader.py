from typing import Union, List

from selenium import webdriver
from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
import concurrent.futures
import time


def read(url: str) -> Union[str, None]:
    """
    Renders the page and returns text from paragraphs
    TODO: error handling
    :param url:
    :return:
    """
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

    return content


def read_many(urls: List[str]) -> List[str]:
    """
    Reads multiple pages concurrently
    :param urls:
    :return:
    """
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(read, url) for url in urls]
        return [future.result() for future in concurrent.futures.as_completed(futures)]


def test():
    urls = [
        "https://nylcv.org/news/psc-denies-renewable-energy-price-adjustments/",
        "https://www.eia.gov/outlooks/steo/report/electricity.php",
    ]

    for result in read_many(urls):
        print(result)


if __name__ == '__main__':
    test()
