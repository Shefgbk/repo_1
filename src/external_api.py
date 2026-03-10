import os
from typing import Any

import requests
from dotenv import load_dotenv


def convert_currency(transaction: dict[Any]) -> float:
    load_dotenv()
    API_KEY = os.getenv('API_KEY')
    if transaction['operationAmount']['currency']['code'] in ['EUR', 'USD']:
        url = (f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/"
               f"{transaction['operationAmount']['currency']['code']}/RUB/"
               f"{transaction['operationAmount']['amount']}")
        response = requests.get(url)
        total_amount = response.json()
        return round(float(total_amount['conversion_result']), 2)
    elif transaction['operationAmount']['currency']['code'] == 'RUB':
        return round(float(transaction['operationAmount']['amount']), 2)
    else:
        return print('Некорректная валюта операции')
# tr = {
#     "id": 41428829,
#     "state": "EXECUTED",
#     "date": "2019-07-03T18:35:29.512364",
#     "operationAmount": {
#       "amount": "8221.37",
#       "currency": {
#         "name": "USD",
#         "code": "USD"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "MasterCard 7158300734726758",
#     "to": "Счет 35383033474447895560"
#   }
#
# convert_currency(tr)
