import api
import logbook

logbook.RotatingFileHandler('my_search_api', level=logbook.TRACE).push_application()
logger = logbook.Logger("Main")

def main():
    logger.info('Taking user input...')
    user_input = input('Enter search criteria: ')
    logger.info(f'Searching for {user_input}')
    result = api.search(user_input)
    print(f'Found {len(result)} results')
    for r in result:
        print(f"Title: {r.get('title')}")
    logger.info('End of execution')

if __name__ == '__main__':
    main()
