import logging
logging.basicConfig(level = logging.INFO)

from urllib.error import HTTPError

import requests

from .utils.news_feed import Feed

from .config import web_scrapping

logger = logging.getLogger(__name__)

def _news_scrapper(news_site, site):
    news = []
    for x in range(1, 100):
        try:
            feed = Feed(news_site[site], news_site[site]['url'].replace('$PAGE', str(x)))
            news.append(feed.article_object)
        except requests.HTTPError as exception:
            print(exception)
            break
    return news

def load():
    config = web_scrapping()
    news_eltiempo = _news_scrapper(config['news_sites'], 'eltiempo')

    return news_eltiempo
