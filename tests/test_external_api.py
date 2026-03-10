import pytest
import os
from unittest.mock import Mock, patch
from dotenv import load_dotenv
from src.external_api import convert_currency

load_dotenv()
API_KEY = os.getenv('API_KEY')

tr1 = {                             # тестовая транзакция
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "18221.37",
      "currency": {
        "name": "руб",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }

def test_convert_currency_rub():            # Тестирование работы функции без конвертации
    assert convert_currency(tr1) == 18221.37

tr2 = {                             # Тестовая транзакция
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }

@patch('requests.get')
def test_convert_currency_usd(mock_get):            # Тестирование конвертации с "заглушкой" обращения к API
    mock_get.return_value.json.return_value = {'conversion_result': 640055.03}
    assert convert_currency(tr2) == 640055.03
    mock_get.assert_called_once_with(f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/"
               f"{tr2['operationAmount']['currency']['code']}/RUB/"
               f"{tr2['operationAmount']['amount']}")

tr3 = {                             # Тестовая транзакция
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "CNY",
        "code": "CNY"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }

def test_convert_currency_cny():            # Тестирование работы функции для неподдерживаемой валюты операции
    assert convert_currency(tr3) == None
