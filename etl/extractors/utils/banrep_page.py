import requests
import bs4

class Inflation:
    def __init__(self, config, url):
        self._config = config
        self._queries = self._config['queries']
        self._html = None

        self._visit(url)

    def _visit(self, url):
        response = requests.get(url, verify=False)
        response.raise_for_status()

        self._html = bs4.BeautifulSoup(response.text, 'html.parser')

    def _to_pandas(self):
        pass