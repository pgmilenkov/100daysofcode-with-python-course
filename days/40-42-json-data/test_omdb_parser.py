import pytest

from omdb_parse import load_movie_data, parse_value

def test_load_movie_data():
    movie_data_it = load_movie_data('It')
    assert movie_data_it != None

    assert 'Title' in movie_data_it
    assert 'It' == movie_data_it['Title']
    assert 'Year' in movie_data_it
    assert 'Awards' in movie_data_it

def test_load_movie_data_empty_name():
    empty_name = load_movie_data('')
    assert empty_name != None
    assert 'Response' in empty_name
    assert 'Error' in empty_name

@pytest.mark.parametrize("arg,ret", [
    ('0%','0.0/10'),
    ('1%','0.1/10'),
    ('100%','10.0/10'),
    ('67%','6.7/10'),
    ('0/100','0.0/10'),
    ('1/100','0.1/10'),
    ('100/100','10.0/10'),
    ('67/100','6.7/10'),
    ('0/10','0.0/10'),
    ('1/10','1.0/10'),
    ('10/10','10.0/10'),
    ('6.7/10','6.7/10'),
])
def test_parse_value(arg, ret):
    assert ret == parse_value(arg)
