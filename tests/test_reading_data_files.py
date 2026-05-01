import unittest
from unittest.mock import mock_open, patch

import pandas as pd

from src.reading_data_files import reading_csv, reading_excel


class TestReadFileFunctions(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open,
           read_data='id;state;date;amount;currency_name;currency_code;from;to;description\n'
                     '4234093;EXECUTED;2021-07-08T07:31:21Z;23182;Ruble;RUB;'
                     'Visa_0773092093872450;Discover_8602781449570491;Перевод_с_карты_на_карту')

    def test_reading_csv(self, mock_file: list[dict]) -> None:
    # Проверка корректности чтения CSV файла
        expected_result = [
            {
                'id': 4234093,
                'state': 'EXECUTED',
                'date': '2021-07-08T07:31:21Z',
                'amount': 23182,
                'currency_name': 'Ruble',
                'currency_code': 'RUB',
                'from': 'Visa_0773092093872450',
                'to': 'Discover_8602781449570491',
                'description': 'Перевод_с_карты_на_карту'
            }
        ]
        result = reading_csv('.data/transactions.csv')
        self.assertEqual(result, expected_result)

    @patch('pandas.read_excel')
    def test_reading_excel(self, mock_reading_excel: list[dict]) -> None:
        # Создаем пример данных для Excel файла
        mock_data = pd.DataFrame({
            'id': [4234093],
            'state': ['EXECUTED'],
            'date': ['2021-07-08T07:31:21Z'],
            'amount': [23182],
            'currency_name': ['Ruble'],
            'currency_code': ['RUB'],
            'from': ['Visa_0773092093872450'],
            'to': ['Discover_8602781449570491'],
            'description': ['Перевод_с_карты_на_карту']
        })
        mock_reading_excel.return_value = mock_data

        # Проверяем, что функция корректно читает Excel файл
        expected_result = [
            {
                'id': 4234093,
                'state': 'EXECUTED',
                'date': '2021-07-08T07:31:21Z',
                'amount': 23182,
                'currency_name': 'Ruble',
                'currency_code': 'RUB',
                'from': 'Visa_0773092093872450',
                'to': 'Discover_8602781449570491',
                'description': 'Перевод_с_карты_на_карту'
            }
        ]
        result = reading_excel('./data/transactions_excel.xlsx')
        self.assertEqual(result, expected_result)
