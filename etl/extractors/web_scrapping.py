import logging
logging.basicConfig(level = logging.INFO)


from utils.news_feed import Feed
from utils.dane_page import Unemployement
from utils.banrep_page import Inflation

from config import web_scrapping

logger = logging.getLogger(__name__)

def _news_scrapper(news_site):
    return Feed(news_site['eltiempo'], news_site['eltiempo']['url'])

def _dane_scrapper(news_site):
    page = Unemployement(news_site['employe'], news_site['employe']['url'])
    return page

def _banrep_scrapper(news_site):
    return Inflation(news_site['statistics'], news_site['statistics']['url'])

def load():
    config = web_scrapping()

    #news = _news_scrapper(config['news_sites'])
    dane = _dane_scrapper(config['dane_sites'])
    #banrep = _banrep_scrapper(config['banrep_sites'])
    print(dane._to_pandas())
    #return news._to_pandas(), dane._to_pandas(), banrep._to_pandas()

load()