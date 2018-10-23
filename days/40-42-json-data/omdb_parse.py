import json
from pprint import pprint
import requests

user_input = input('Movie name: ')

request = requests.get('http://www.omdbapi.com/?apikey=3e6f7dd7&t={}'.format(user_input))
json_result = json.loads(request.text)

print("{}'s Awards: {}".format(user_input, json_result['Awards']))


def parse_value(value: str):
    if value.endswith('%'):
        value = value.replace('%','')
        return '{}/10'.format(int(value) / 10)
    elif value.endswith('100'):
        (value, _) = value.split('/')
        return '{}/10'.format(int(value) / 10)
    return value


def display_rating(rating):
    value = rating['Value']
    value = parse_value(value)
    print(f"{rating['Source']} - {value}")


for rating in json_result['Ratings']:
    display_rating(rating)
