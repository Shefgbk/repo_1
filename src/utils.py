import json
from json import JSONDecodeError
from typing import Any


def transactions_list(filename: Any = None) -> list[dict[Any, Any]]:
    '''Функция, которая принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях'''
    result_list = []
    try:
        with open(filename, 'r', encoding="utf-8") as f:
            result_list = list(json.load(f))
        return result_list
    except FileNotFoundError:  # Файл не найден
        print('Файл не найден')
        return result_list
    except JSONDecodeError:  # Некорректный формат файла
        print('Некорректный формат данных')
        return result_list
    except TypeError:
        print('Файл не указан')  # Файл не указан
        return result_list
