from pathlib import Path

from src.utils import transactions_list


def test_transactions_list_empty_filename() -> None:        # Тестирование функции без указания файла
    assert transactions_list() == []


def test_transactions_list_incorrect_filename() -> None:      # Тестирование функции c указанием несуществующего файла
    assert transactions_list(Path('./data/operation.json').resolve()) == []


def test_transactions_list_incorrect_data() -> None:   # Тестирование функции c некорректным форматом содержимого файла
    assert transactions_list(Path('./data/operations_incorrect.json').resolve()) == []


def test_transactions_list_correct_data() -> None:     # Тестирование функции c корректным форматом содержимого файла
    assert transactions_list(Path('./data/operations.json').resolve()) != []
