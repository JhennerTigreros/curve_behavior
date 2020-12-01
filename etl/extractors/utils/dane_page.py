import requests
import bs4
import pandas as pd

class Unemployement:
    def __init__(self, config, url):
        self._config = config
        self._queries = self._config['queries']
        self._html = None

        self._visit(url)

    def _visit(self, url):
        response = requests.get(url, verify=False)
        response.raise_for_status()
        self._html = bs4.BeautifulSoup(response.text, 'html.parser')

    @property
    def excel(self):
        link_excel = ''
        for link in self._select(self._queries['select_table_content']):
            if link and link.has_attr('href') and "desestacionalizado" in link['href']:
                link_excel = link

        return link_excel

    def _select(self, query_string):
        return self._html.select(query_string)

    def _to_pandas(self):
        print(self._config['base'] + self.excel['href'])
        return pd.read_excel(self._config['base'] + self.excel['href'], sheet_name='Tnal mensual')