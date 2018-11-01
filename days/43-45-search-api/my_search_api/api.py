from typing import List

import requests
from collections import namedtuple

Movie = namedtuple('Movie', 'imdb_code, title, director, keywords, duration,'
                            'genres, rating, year, imdb_score')

def search(keyword: str) -> List[Movie]:
    url = f'http://movie_service.talkpython.fm/api/search/{keyword}'

    response = requests.get(url)
    response.raise_for_status()

    movies = []
    for movie in response.json()['hits']:
        movies.append(Movie(**movie))

    return movies
