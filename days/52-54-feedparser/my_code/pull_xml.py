import requests


def day1():
    URL = "http://store.steampowered.com/feeds/newreleases.xml"
    r = requests.get(URL)
    r.raise_for_status()

    with open("my_file_day1.xml", "w") as f:
        f.write(r.text)


def day2():
    URL = "https://www.sportal.bg/uploads/rss_category_0.xml"
    r = requests.get(URL)
    r.raise_for_status()

    with open("my_file_day2.xml", "w", encoding='iso_8859_1') as f:
        f.write(r.text)


def main():
    # day1()
    day2()



if __name__ == '__main__':
    main()
