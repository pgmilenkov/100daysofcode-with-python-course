import api
import logbook
from webbrowser import open as web_open

logbook.RotatingFileHandler('my_search_api', level=logbook.TRACE).push_application()
logger = logbook.Logger("Main")

def main():
    logger.info('Taking user input...')
    user_input = input('Enter search criteria: ')
    logger.info(f'Searching for {user_input}')
    articles = api.search(user_input)
    print(f'Found {len(articles)} articles')
    id_to_article_dict = {}
    for r in articles:
        id_to_article_dict[r.id] = r
        print(f"[{r.id}] {r.title}: {r.category}")

    print("*"*20)

    user_input = input('For which article do you need more information [q for quit]: ')
    if user_input != 'q':
        web_open("http://talkpython.fm" + id_to_article_dict[int(user_input)].url, new=2)
    logger.info('End of execution')

if __name__ == '__main__':
    main()
