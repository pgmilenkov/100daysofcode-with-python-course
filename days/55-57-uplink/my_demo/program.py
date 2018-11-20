
from api import API


MENU_OPTIONS = ['Search By Keyword',
                'Get Director Info by Name',
                'Get Movie Info by IMDB ID']

MENU_OPTIONS_TO_FUNC_MAP = {
    1: {
        'function_name': 'search_by_keyword',
        'parameter_name': 'keyword'
    },
    2: {
        'function_name': 'get_director_by_name',
        'parameter_name': 'director name'
    },
    3: {
        'function_name': 'get_movie_by_imdb_number',
        'parameter_name': 'imdb number'
    }
}

def display_menu():
        for id, option in enumerate(MENU_OPTIONS, start=1):
            print(f'[{id}]. {option}')


def get_user_choice():
    user_selection = input('Select: ')
    try:
        user_selection = int(user_selection)
    except ValueError as e:
        print(e)
        exit(1)
    return user_selection

def main():
    display_menu()
    user_selection = get_user_choice()
    function_name = MENU_OPTIONS_TO_FUNC_MAP[user_selection]['function_name']
    parameter_name = MENU_OPTIONS_TO_FUNC_MAP[user_selection]['parameter_name']
    parameter_value = input(f'Please enter {parameter_name}: ')

    api = API()
    function_to_call = api.__getattribute__(function_name)
    response = function_to_call(parameter_value)

    if response.json() is None:
        print('Could not find anything with this information.')
        exit(1)
    # response = api.search_by_keyword('movie')
    for entry in response.json():
        print(f'{entry}')

    # print()
    #
    # response = api.get_director_by_name('Cameron')
    # for entry in response.json()['hits']:
    #     print(entry)
    #
    # print()
    #
    # response = api.get_movie_by_imdb_number('tt0499549')
    # movie_info = response.json()
    # print('{}'.format(entry['imdb_score']))
    # for entry in movie_info:




if __name__ == '__main__':
    main()
