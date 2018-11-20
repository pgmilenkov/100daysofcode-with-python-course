import logbook
import api

logbook.RotatingFileHandler('sportal_scraper.log').push_application()
logger = logbook.Logger('Main')


def main():
    logger.info('Starting application...')
    api.download_site('https://www.sportal.bg')
    top_news = api.get_top_news()
    api.look_for_pattern(top_news, 'Мадрид')
    api.look_for_pattern(top_news, 'Барселона')

if __name__ == '__main__':
    main()
