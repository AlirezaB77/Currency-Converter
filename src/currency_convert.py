import requests
from cachetools import cached, TTLCache

cache = TTLCache(maxsize=100, ttl=3*60*60)

@cached(cache)
def get_exchange_rate(base_currency , target_currency):
    url = f'https://v6.exchangerate-api.com/v6/580873e082b895eb9f4693f3/latest/{base_currency}'
    response = requests.get(url)
    exchange_rate = response.json()['conversion_rates'][target_currency]
    last_time_update = response.json()['time_last_update_unix']
    return exchange_rate,last_time_update

def convert_currency(amount,exchange_rate):
    return amount * exchange_rate

