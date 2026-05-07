from typing import Iterator


def filter_by_currency(transactions: list[dict], curr: str) -> Iterator:
    ''' Функция принимает на вход список словарей, представляющих транзакции.
    Возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD) '''
    list_values = []
    for transaction in transactions:
        if len(transaction) == 7:
            list_values.append(transaction['operationAmount']['currency']['code'])
        elif len(transaction) == 9:
            list_values.append(transaction['currency_code'])
    if len(transactions[0]) == 7:
        if curr in list_values:
            return (transaction for transaction in transactions
                    if transaction['operationAmount']['currency']['code'] == curr)
        else:
            print('Нет транзакций в указанной валюте')
            return iter([])
    elif len(transactions[0]) == 9:
        if curr in list_values:
            return (transaction for transaction in transactions
                    if transaction['currency_code'] == curr)
        else:
            print('Нет транзакций в указанной валюте')
            return iter([])
    else:
        print('Некорректный формат данных')
        return iter([])


def transaction_descriptions(transactions: list[dict]) -> Iterator:
    ''' Генератор, который принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди '''
    if transactions:
        for transaction in transactions:
            yield transaction['description']
    else:
        print('Отсутствуют транзакции для вывода')


def card_number_generator(start: int, end: int) -> Iterator:
    ''' Генератор номеров карт в заданном диапазоне от 0000 0000 0000 0001
    до 9999 9999 9999 9999 (начало и конец диапазона задаются вручную) '''
    if start in range(1, 10000000000000000) and end in range(1, 10000000000000000):
        for num in range(start, end + 1):
            str_num = str(num)
            while len(str_num) < 16:
                str_num = '0' + str_num
            card_num = str_num[:4] + ' ' + str_num[4:8] + ' ' + str_num[8:12] + ' ' + str_num[12:]
            yield card_num
    else:
        print('Задан некорректный диапазон номеров карт')


# Тестовые данные:
transactions = (
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)

transactions2 = (
    [
        {'id': 3330422, 'state': 'EXECUTED', 'date': '2023-08-05T07:11:26Z', 'amount': 14175,
         'currency_name': 'Ruble', 'currency_code': 'RUB', 'from': 'Mastercard 9458117363112215',
         'to': 'Visa 6335859532296628', 'description': 'Перевод с карты на карту'},
        {'id': 3794942, 'state': 'EXECUTED', 'date': '2021-05-24T02:37:49Z', 'amount': 14174,
         'currency_name': 'Yuan Renminbi', 'currency_code': 'CNY', 'from': 'Mastercard 8628645140673956',
         'to': 'Счет 36990402090010935845', 'description': 'Перевод организации'},
        {'id': 3616670, 'state': 'EXECUTED', 'date': '2020-06-03T13:14:27Z', 'amount': 18397,
         'currency_name': 'Dollar', 'currency_code': 'USD', 'from': 'Discover 7364800433362108',
         'to': 'Visa 4397277168551394', 'description': 'Перевод с карты на карту'},
        {'id': 3967324, 'state': 'EXECUTED', 'date': '2021-05-22T07:46:10Z', 'amount': 30809,
         'currency_name': 'Peso', 'currency_code': 'PHP', 'from': None, 'to': 'Счет 99143269778241825075',
         'description': 'Открытие вклада'},
        {'id': 3236978, 'state': 'EXECUTED', 'date': '2023-02-07T04:25:44Z', 'amount': 12642,
         'currency_name': 'Dollar', 'currency_code': 'USD', 'from': 'Mastercard 4156625376917975',
         'to': 'American Express 6573309743396617', 'description': 'Перевод с карты на карту'}
    ]
)
