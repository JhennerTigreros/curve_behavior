import yaml

__gov_api_config = None
__twitter_api_config = None
__web_scrapping_config = None

def gov_config():
    global __gov_api_config

    if not __gov_api_config:
        with open('./configs/gov_api.yaml', mode = 'r') as f:
            __gov_api_config = yaml.load(f)

    return __gov_api_config

def twitter_conifg():
    global __twitter_api_config

    if not __twitter_api_config:
        with open('./configs/twitter_api.yaml', mode = 'r') as f:
            __twitter_api_config = yaml.load(f)

    return __twitter_api_config

def web_scrapping():
    global __web_scrapping_config

    if not __web_scrapping_config:
        with open('./configs/web_scrapping.yaml', mode = 'r') as f:
            __web_scrapping_config = yaml.load(f)

    return __web_scrapping_config