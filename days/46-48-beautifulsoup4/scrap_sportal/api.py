from typing import List

import logbook
import requests
import bs4
import os

from bs4 import Tag


def file_exists(file_name):
    return os.path.isfile(file_name)

def download_site(url):
    if file_exists('sportal.html'):
        print("Not downloading...")
        return

    response = requests.get(url)
    response.raise_for_status()
    with open('sportal.html', 'w') as f:
        f.write(response.text)


def get_top_news() -> List[Tag]:
    top_news = []
    with open('sportal.html') as f:
        soup = bs4.BeautifulSoup(f, 'html.parser')
    for item in soup.select('.orange_link'):
        top_news.append(item)

    return top_news

def look_for_pattern(news: List[Tag], pattern):
    for item in news:
        if pattern in item.text:
            print(f'Title {item.text}: link https://www.sportal.bg/{item.get("href")}')

