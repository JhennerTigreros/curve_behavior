from searchtweets import ResultStream, gen_request_parameters, load_credentials, collect_results
import datetime
from functools import reduce
from .config import twitter_conifg

def load():
    config = twitter_conifg()
    base_date = datetime.datetime.today()
    date_list = [ base_date - datetime.timedelta(days = x) for x in range(5)]
    date_list.reverse()
    all_tweets = []
    for idx, date in enumerate(date_list):
        if idx != 4:
            final_date = date + datetime.timedelta(days = 1)
            search_args = load_credentials(filename="./configs/twitter_api.yaml",
                            yaml_key="search_tweets_v2",
                            env_overwrite=False)

            query = gen_request_parameters(config['query'], results_per_call=100,
                        place_fields='country', start_time=date.strftime('%Y-%m-%d'), end_time=final_date.strftime('%Y-%m-%d'))

            tweets = collect_results(query,
                                    max_tweets=1000,
                                    result_stream_args=search_args)

            def add_date(x):
                x['fecha'] = date.strftime('%Y-%m-%d')

                return x
            tweets = list(map(add_date, tweets))
            all_tweets.append(tweets)

    all_tweets = reduce(lambda x, y: x + y, all_tweets)
    return all_tweets
