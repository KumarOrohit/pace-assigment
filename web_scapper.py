import requests
from bs4 import BeautifulSoup
import time
import json

while True:
    try:
        r = requests.get('https://coinmarketcap.com/')
    except Exception as e:
        print(e)
        time.sleep(10)
        continue

    soup = BeautifulSoup(r.content, 'html.parser')
    data_table = soup.find('table', class_="h7vnx2-2 juYUEZ cmc-table")
    data_body = data_table.find('tbody')
    data_column = data_body.find_all('tr')

    result = []
    for i in range(len(data_column)):
            scrap_data = data_column[i].find_all('td')

            if len(scrap_data) < 9:
                continue
            name = scrap_data[2].find('p').text
            price = scrap_data[3].find('a').find('span').text
            h1 = scrap_data[4].find('span').text
            h24 = scrap_data[5].find('span').text
            d7 = scrap_data[6].find('span').text
            market_cap = scrap_data[7].find('span').text
            volume_24h = scrap_data[8].find('p').text
            circulating_supply = scrap_data[9].find('p').text

            result_dict = {
                "name": name,
                "price": price,
                "h1": h1,
                "h24": h24,
                "d7": d7,
                "market_cap": market_cap,
                "volume_24h": volume_24h,
                "circulating_supply": circulating_supply
            }

            result.append(result_dict)

    url = 'http://127.0.0.1:8000//web-scrap/scrap-data'

    payload = json.dumps(result)

    headers = {
        'Content-Type': 'application/json',
        'Cookie': 'csrftoken=Dln8aRlBb7D56eP5uV6ZcCn5HYGx0iHHl0g6X4Q7EkJMLOvc5OoHyFhDb0gbHJXr'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 200:
        print('Sucess')
        time.sleep(5)
    else:
        print(response)
        time.sleep(10)