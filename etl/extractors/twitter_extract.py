from searchtweets import ResultStream, gen_request_parameters, load_credentials, collect_results
import datetime
from functools import reduce

def load():
    final_date = datetime.datetime.today()
    initial_date = final_date - datetime.timedelta(days = 5)
    all_tweets = []
    for delta in range(5, 0, -1):
        date_0 = initial_date + datetime.timedelta(days = delta)
        date_1 = initial_date + datetime.timedelta(days = delta + 1)
        search_args = load_credentials(filename="./configs/twitter_api.yaml",
                        yaml_key="search_tweets_v2",
                        env_overwrite=False)

        query = gen_request_parameters("covid19 colombia lang:es", results_per_call=100,
                    place_fields='country', start_time=date_0.strftime('%Y-%m-%d'), end_time=date_1.strftime('%Y-%m-%d'))

        tweets = collect_results(query,
                                max_tweets=1000,
                                result_stream_args=search_args)

        def add_date(x):
            x['fecha'] = date_0.strftime('%Y-%m-%d')

            return x
        tweets = list(map(add_date, tweets))
        all_tweets.append(tweets)

    all_tweets = reduce(lambda x, y: x + y, all_tweets)
    return all_tweets
