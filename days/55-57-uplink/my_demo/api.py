import uplink
import requests
from uplink_helpers import raise_for_status


@raise_for_status
@uplink.json
class API(uplink.Consumer):
    def __init__(self):
        super().__init__(base_url='http://movie_service.talkpython.fm/')


    @uplink.get('/api/search/{keyword}')
    def search_by_keyword(self, keyword) -> requests.models.Response:
        ''' Search by given keyword'''


    @uplink.get('/api/director/{director_name}')
    def get_director_by_name(self, director_name) -> requests.models.Response:
        ''' Geti director by name '''

    @uplink.get('/api/movie/{imdb_number}')
    def get_movie_by_imdb_number(self, imdb_number) -> requests.models.Response:
        ''' Get movie by imdb number'''
