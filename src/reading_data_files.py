from typing import Any

import pandas as pd


def reading_csv(file_path: str) -> list[dict[Any, Any]]:    # Пример file_path: './data/transactions.csv'
    ''' Функция для считывания финансовых операций из CSV
    принимает путь к файлу CSV в качестве аргумента '''
    dict_df_csv = pd.read_csv(file_path, delimiter=';').to_dict(orient='records')
    return dict_df_csv


def reading_excel(file_path: str) -> list[dict[Any, Any]]:    # Пример file_path: './data/transactions_excel.xlsx'
    ''' Функция для считывания финансовых операций из Excel
    принимает путь к файлу Excel в качестве аргумента '''
    dict_df_excel = pd.read_excel(file_path).to_dict(orient='records')
    return dict_df_excel
