import json
from pprint import pprint
import requests
import logbook
from log_book import init_logger

logger = logbook.Logger(__file__)


def main():
    init_logger('movie-app.log')
    logbook.info("Starting the omdb search app...")

    logbook.debug("Getting user's input...")
    movie_name = get_user_input()

    logbook.debug("Loading '{0}' data...".format(movie_name))
    movie_data = load_movie_data(movie_name)


    logbook.debug("Displaying Awards...".format(movie_name))
    display_awards(movie_data, movie_name)

    logbook.debug("Displaying Ratings...".format(movie_name))
    displays_ratings(movie_data)

def get_user_input():
    user_input = input('Movie name: ')
    return user_input

def load_movie_data(movie_name):
    request = requests.get('http://www.omdbapi.com/?apikey=3e6f7dd7&t={}'.format(movie_name))
    json_result = json.loads(request.text)
    return json_result

def display_awards(movie_data, movie_name):
    print("{}'s Awards: {}".format(movie_name, movie_data['Awards']))

def displays_ratings(movie_data):
    for rating in movie_data['Ratings']:
        display_rating(rating)

def display_rating(rating):
    value = rating['Value']
    value = parse_value(value)
    print(f"{rating['Source']} - {value}")

def parse_value(value: str):
    logbook.debug("Parsing value '{0}'...".format(value))
    if value.endswith('%'):
        value = value.replace('%','')
        return '{}/10'.format(int(value) / 10)
    elif value.endswith('100'):
        (value, _) = value.split('/')
        return '{}/10'.format(int(value) / 10)
    else:
        (value, _) = value.split('/')
        return '{}/10'.format(float(value) * 1.0)



if __name__ == '__main__':
    main()
