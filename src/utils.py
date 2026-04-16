import json
import logging
import os
from json import JSONDecodeError
from typing import Any

current_dir = os.path.dirname(os.path.abspath(__file__))

rel_file_path = os.path.join(current_dir, "../logs/utils.log")
abs_file_path = os.path.abspath(rel_file_path)

logger = logging.getLogger('utils')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(abs_file_path, 'w', encoding="utf-8")
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def transactions_list(filename: Any = None) -> list[dict[Any, Any]]:
    '''Функция, которая принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях'''
    result_list = []
    try:
        logger.info('Получение списка финансовых операций')
        with open(filename, 'r', encoding="utf-8") as f:
            result_list = list(json.load(f))
        logger.info('Получен список финансовых операций')
        return result_list
    except FileNotFoundError:  # Файл не найден
        logger.error('Файл не найден')
        print('Файл не найден')
        return result_list
    except JSONDecodeError:  # Некорректный формат файла
        logger.error('Некорректный формат данных')
        print('Некорректный формат данных')
        return result_list
    except TypeError:
        logger.error('Файл не указан')
        print('Файл не указан')  # Файл не указан
        return result_list
