import os
from unittest.mock import Mock, patch

from dotenv import load_dotenv

from src.external_api import convert_currency

load_dotenv()
API_KEY = os.getenv('API_KEY2')

tr1 = {                             # Тестовая транзакция
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


def test_convert_currency_rub() -> None:            # Тестирование работы функции без конвертации
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
def test_convert_currency_usd(mock_get: dict) -> None:         # Тестирование конвертации с "заглушкой" обращения к API
    mock_get.return_value.json.return_value = {'result': 640055.03}
    assert convert_currency(tr2) == 640055.03
    mock_get.assert_called_once_with(f"https://api.apilayer.com/exchangerates_data/convert?to="
                                     f"{'RUB'}&from={tr2['operationAmount']['currency']['code']}"
                                     f"&amount={tr2['operationAmount']['amount']}", {'apikey': API_KEY})


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


def test_convert_currency_cny() -> None:            # Тестирование работы функции для неподдерживаемой валюты операции
    assert convert_currency(tr3) is None


tr4 = {                             # Тестовая транзакция
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


def test_api_no_key() -> None:      # Тестирование работы функции с отстутствующим API-ключом в файле .env
    os.getenv = Mock(return_value=None)
    result = convert_currency(tr4)
    assert result is None
