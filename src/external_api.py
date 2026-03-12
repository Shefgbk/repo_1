import os
from typing import Any

import requests
from dotenv import load_dotenv


def convert_currency(transaction: dict[Any]) -> float:
    '''Функция, которая принимает на вход транзакцию и
    возвращает сумму транзакции в рублях'''
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
        return None
        print('Некорректная валюта операции')
