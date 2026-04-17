import os
from typing import Any

import requests
from dotenv import load_dotenv


def convert_currency(transaction: dict[Any, Any]) -> float | None:
    '''Функция, которая принимает на вход транзакцию и
    возвращает сумму транзакции в рублях'''
    load_dotenv()
    API_KEY = os.getenv('API_KEY2')
    if transaction['operationAmount']['currency']['code'] in ['EUR', 'USD']:
        url = (f"https://api.apilayer.com/exchangerates_data/convert?to="
               f"{'RUB'}&from={transaction['operationAmount']['currency']['code']}"
               f"&amount={transaction['operationAmount']['amount']}")
        headers = {"apikey": API_KEY}
        response = requests.get(url, headers)
        total_amount = response.json()
        return round(float(total_amount['result']), 2)
    elif transaction['operationAmount']['currency']['code'] == 'RUB':
        return round(float(transaction['operationAmount']['amount']), 2)
    else:
        print('Некорректная валюта операции')
        return None
