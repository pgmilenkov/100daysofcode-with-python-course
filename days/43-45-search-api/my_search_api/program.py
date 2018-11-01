import api

def main():
    keyword = input('Enter search term: ')
    results = api.search(keyword)
    print(f'There are {len(results)} movies found')
    for movie in results:
        print(f'{movie.title}: has score {movie.imdb_score}')

if __name__ == '__main__':
    main()
