import json
from json import JSONDecodeError


def transactions_list(filename: str = None) -> list[dict]:
    result_list = []
    try:
        with open(filename, 'r', encoding="utf-8") as f:
            result_list = json.load(f)
        return result_list
    except FileNotFoundError:  # Файл не найден
        return result_list
    except JSONDecodeError:  # Некорректный формат файла
        return result_list
    except TypeError:  # Файл не указан
        return result_list


way = 'data\\operations.json'
print(transactions_list(way))
