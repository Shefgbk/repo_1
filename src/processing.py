from datetime import datetime
import re
from re import search
from collections import Counter


def filter_by_state(dic_list: list, state: str = 'EXECUTED') -> list:
    ''' Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state (по умолчанию 'EXECUTED') соответствует указанному значению '''
    filtred_dic_list = []
    for dic in dic_list:
        if dic.get('state', '').lower() == state.lower():
            filtred_dic_list.append(dic)
    if filtred_dic_list != []:
        return filtred_dic_list
    else:
        raise ValueError(f'Словари со статусом {state} отсутствуют')


def sort_by_date(dict_list: list, descending: bool = True) -> list:
    ''' Функция возвращает новый список словарей,
    отсортированных по дате (по умолчанию — убывание) '''
    sorted_list = sorted(dict_list, key=lambda x: datetime.fromisoformat(x['date']), reverse=descending)
    return sorted_list


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    ''' Функция, которая принимает список словарей с данными о банковских операциях
    и строку поиска, возвращает список словарей, у которых в описании есть данная строка'''
    pattern = rf'{search.lower()}'
    searched_dicts = [item for item in data if re.search(pattern, item['description'].lower())]
    if searched_dicts:
        return searched_dicts
    else:
        print('\nТранзакции с данным типом операции не найдены')
        return None


def process_bank_operations(data: list[dict], categories: list) -> dict:
    ''' Функция, которая принимает список словарей с данными о банковских операциях
    и список категорий операций, а возвращает словарь, в котором ключи —
    это названия категорий, а значения — это количество операций в каждой категории '''
    oper_categories = []
    for item in data:
        oper_categories.append(item['description'])
    count = Counter(oper_categories)
    result = {}
    for cat in categories:
        result[cat] = count.get(cat, 0)
    return dict(result)


categories = ['Открытие вклада', 'Перевод организации', 'Перевод со счета на счет', 'Перевод с карты на карту']
data_1 = [
    {
    "id": 542678139,
    "state": "CANCELED",
    "date": "2018-10-14T22:27:25.205631",
    "operationAmount": {
      "amount": "90582.51",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Visa Platinum 2256483756542539",
    "to": "Счет 78808375133947439319"
  },
  {
    "id": 558167602,
    "state": "EXECUTED",
    "date": "2019-04-12T17:27:27.896421",
    "operationAmount": {
      "amount": "43861.89",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 73654108430135874305",
    "to": "Счет 89685546118890842412"
  },
  {
    "id": 407169720,
    "state": "EXECUTED",
    "date": "2018-02-03T14:52:08.093722",
    "operationAmount": {
      "amount": "67011.26",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод с карты на карту",
    "from": "MasterCard 4047671689373225",
    "to": "Maestro 3806652527413662"
  },
  {
    "id": 361044570,
    "state": "EXECUTED",
    "date": "2018-03-02T02:03:11.563721",
    "operationAmount": {
      "amount": "7484.91",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 96008924215040031147",
    "to": "Счет 30377212495530283001"
  }
]
