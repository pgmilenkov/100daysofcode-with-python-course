from typing import List

import requests
from collections import namedtuple

Article = namedtuple('Article', 'category, id,'
                                'url, title, description')

def search(keyword: str) -> List[Article]:
    print(f'Looking for {keyword}...')

    url = f'http://search.talkpython.fm/api/search?q={keyword}'
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        print('Cannot connect. Please try again later.')
        return []
    response.raise_for_status()

    articles = []
    for article in response.json()['results']:
        articles.append(Article(**article))
    return articles
