import requests
from bs4 import BeautifulSoup


def scrapy(url: str, selector: str, word: str) -> object:
    word.lower()
    url += word
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    titles = soup.select(selector)
    return titles
