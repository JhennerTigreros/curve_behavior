import sys
import logging
logging.basicConfig(level = logging.INFO)

from datetime import datetime, timedelta
import pandas as pd
from config import gov_config

logger = logging.getLogger(__name__)

def get_data(url, filters = ''):
    return pd.read_csv(url + filters)

def load():
    config = gov_config()

    initial_date = datetime.strptime(config['initial_date'], '%d/%m/%Y %H:%M:%S')
    final_date = datetime.today()

    diff = abs((final_date - initial_date).days)

    column_names_daily_cases = config['daily_cases']['column_names']
    column_names_test = config['test']['column_names']

    df_daily_cases = pd.DataFrame(columns = column_names_daily_cases)
    df_daily_test = pd.DataFrame(columns = column_names_test)

    date_filter_daily_cases = config['daily_cases']['filters']['date']

    url_daily_cases = config['daily_cases']['url']
    url_test_cases = config['test']['url']

    for delta in range(diff):
        date = initial_date + timedelta(days = delta)
        df_daily_cases = pd.DataFrame.append(df_daily_cases, get_data(url_daily_cases, date_filter_daily_cases.replace('DATE', date.strftime('%-d/%-m/%Y %-H:%M:%S')).replace(' ', '%20')))

    df_daily_test = pd.DataFrame.append(df_daily_test, get_data(url_test_cases))

    return df_daily_cases, df_daily_test