import re
from pprint import pprint
import logbook


import requests
import bs4


logbook.RotatingFileHandler('scrapper.log',level=logbook.TRACE).push_application()
logger = logbook.Logger('scraper')

def get_site(URL):
    logger.debug(f'Getting url {URL}')
    response = requests.get(URL)
    response.raise_for_status()
    logger.debug(f'Successfully retrieved url {URL}')
    return response.text

def main():
    logger.info('Start scraping...')
    site = get_site('http://codechalleng.es/challenges/')
    soup = bs4.BeautifulSoup(site, 'html.parser')

    css_class = '.challengeTitle'
    logger.debug('Looking for class {css_class}')
    challenges = soup.select(css_class)

    challenges_names = []
    logger.info('Iterating over challenges...')
    for challenge in challenges:
        logger.debug('')
        title = re.sub("^\s*[0-9]{2} - ", "", challenge.text)
        title = re.sub("\s*$", "", title)
        challenges_names.append(title)

    print(f'Found {len(challenges_names)} challenges.')
    pprint(challenges_names)

if __name__ == '__main__':
    main()
