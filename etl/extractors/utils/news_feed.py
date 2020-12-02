import requests
import bs4
from datetime import datetime

class Feed:
    def __init__(self, config, url):
        self._config = config
        self._queries = self._config['queries']
        self._html = None

        self._visit(url)

    @property
    def articles(self):
        articles = []

        for article in self._select(self._queries['articles']):
            articles.append(article)

        return articles

    @property
    def article_object(self):
        articles = self.articles
        objects = []
        for article in articles:
            objects.append(
                {
                    "title": article.select_one('.title').text,
                    "publised_time": datetime.fromtimestamp(int(article.select_one('.published-at')['published-unix'])),
                    "category": article.select_one('.category').text,
                    "resume": article.select_one('.epigraph').text,
                }
            )
        return objects


    def _select(self, query):
        return self._html.findAll('div', {'class': query})

    def _visit(self, url):
        response = requests.get(url, verify=False)
        response.raise_for_status()

        self._html = bs4.BeautifulSoup(response.text, 'html.parser')