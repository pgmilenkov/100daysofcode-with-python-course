import feedparser
import logbook

logbook.RotatingFileHandler('parser.log').push_application()
logger = logbook.Logger('feed_parser')

def print_feed(feed, selected_tag):
    logger.debug("Trying to print 'published', 'title' and 'link'...")
    selected_feeds = [entry for entry in feed.entries if selected_tag in entry.tags[0].term]
    for entry in selected_feeds:
        try:
            print(f'[{entry.tags[0].term}] {entry.published} - {entry.title}: {entry.link}')
        except AttributeError as error:
            logger.error(f'Could not print some of the attributes of the feed.')
            print(f'Cannot find some of the attributes: {error}')


def main():
    logger.info('Starting the application...')
    selected_tag = input('Preferred tag name:')
    # day1_file = 'my_file_day1.xml'
    # feed = feedparser.parse(day1_file)
    day2_file = 'my_file_day2.xml'
    feed = feedparser.parse(day2_file)
    print_feed(feed, selected_tag)

if __name__ == '__main__':
    main()
