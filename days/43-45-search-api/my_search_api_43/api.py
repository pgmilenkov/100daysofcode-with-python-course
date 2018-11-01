import requests

def search(keyword):
    print(f'Looking for {keyword}...')

    url = f'http://search.talkpython.fm/api/search?q={keyword}'
    response = requests.get(url)
    response.raise_for_status()

    return response.json()['results']
