import os
import json
import requests
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pace.settings')

app = Celery('pace')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def update_web_scrap_data(data):
    scrap_data = requests.get("https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing")

    data_list = scrap_data.json().get('data').get('cryptoCurrencyList')

    result = []

    for data in data_list:
        name = data.get('name')
        circulating_supply = data.get('circulatingSupply')
        price = data.get('quotes')[0].get('price')
        volume24h = data.get('quotes')[0].get('volume24h')
        marketCap = data.get('quotes')[0].get('marketCap')
        percentChange1h = data.get('quotes')[0].get('percentChange1h')
        percentChange24h = data.get('quotes')[0].get('percentChange24h')
        percentChange7d = data.get('quotes')[0].get('percentChange7d')

        result_dict = {
                            "name": name,
                            "price": price,
                            "h1": percentChange1h,
                            "h24": percentChange24h,
                            "d7": percentChange7d,
                            "market_cap": marketCap,
                            "volume_24h": volume24h,
                            "circulating_supply": circulating_supply
                        }

        result.append(result_dict)

    url = 'http://127.0.0.1:8000/web-scrap/scrap-data'

    payload = json.dumps(result)

    headers = {
        'Content-Type': 'application/json',
        'Cookie': 'csrftoken=Dln8aRlBb7D56eP5uV6ZcCn5HYGx0iHHl0g6X4Q7EkJMLOvc5OoHyFhDb0gbHJXr'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 200:
        print('Sucess')
    else:
        print(response)