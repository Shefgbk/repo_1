import re

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions, transactions


def test_filter_by_currency() -> None:      # Тестирование корректной работы фильтрации
    gen = filter_by_currency(transactions, 'USD')
    result = [{
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
        }]
    for _ in range(3):
        assert next(gen) == result[_]


def test_filter_by_currency_incorrect_value() -> None:  # Тестирование с отсутствующей валютой
    with pytest.raises(StopIteration):
        chck_transactions = filter_by_currency(transactions, 'CNY')
        next(chck_transactions)


def test_filter_by_currency_null_value() -> None:  # Тестирование без указания валюты
    with pytest.raises(StopIteration):
        chck_transactions = filter_by_currency(transactions, ' ')
        next(chck_transactions)


@pytest.fixture
def descriptions() -> list[str]:
    return ['Перевод организации',
            'Перевод со счета на счет',
            'Перевод со счета на счет',
            'Перевод с карты на карту',
            'Перевод организации']


def test_transaction_descriptions_5(descriptions: list[str]) -> None:    # Тестирование корректной работы
    tst_description = transaction_descriptions(transactions)             # вывода описаний 5 операций
    for _ in range(5):
        assert next(tst_description) == descriptions[_]


def test_transaction_descriptions_3(descriptions: list[str]) -> None:    # Тестирование корректной работы
    tst_description = transaction_descriptions(transactions)             # вывода описаний 3 операций
    for _ in range(3):
        assert next(tst_description) == descriptions[_]


def test_transaction_descriptions_1(descriptions: list[str]) -> None:    # Тестирование корректной работы
    tst_description = transaction_descriptions(transactions)             # вывода описаний 1 операции
    for _ in range(1):
        assert next(tst_description) == descriptions[_]


def test_transaction_descriptions_null_value() -> None:  # Тестирование пустого списка операций
    with pytest.raises(StopIteration):
        chck_descriptions = transaction_descriptions([])
        next(chck_descriptions)


generated_numbers = ['0000 0000 0000 0010',
                     '0000 0000 0000 0011',
                     '0000 0000 0000 0012',
                     '0000 0000 0000 0013',
                     '0000 0000 0000 0014',
                     '0000 0000 0000 0015']


def test_correct_card_number_generator() -> None:       # Тестирование корректной генерации номеров карт
    gen = card_number_generator(10, 15)
    for _ in range(6):
        assert next(gen) == generated_numbers[_]


@pytest.mark.parametrize('start, stop, expected_cards', [
    (7896000000000004, 7896000000000006, ['7896 0000 0000 0004', '7896 0000 0000 0005', '7896 0000 0000 0006']),
    (9876000000000005, 9876000000000008, ['9876 0000 0000 0005', '9876 0000 0000 0006',
                                          '9876 0000 0000 0007', '9876 0000 0000 0008']),
])
def test_card_number_generator(start: int, stop: int, expected_cards: list[str]) -> None:    # Тестирование генерации
    result = list(card_number_generator(start, stop))                               # номеров на разных диапазонах карт
    assert result == expected_cards


def test_card_number_generator_incorrect_values() -> None:  # Тестирование с некорректным диапазоном номеров карт
    with pytest.raises(StopIteration):
        gen = card_number_generator(-2, 2)
        for _ in range(5):
            print(next(gen))


def test_card_number_generator_format() -> None:    # Тестирование корректности формата генерируемых номеров карт
    gen = card_number_generator(1, 5)
    for _ in range(5):
        assert bool(re.match(r'^\d{4} \d{4} \d{4} \d{4}$', next(gen)))
