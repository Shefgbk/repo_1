from datetime import datetime

from masks import get_mask_account, get_mask_card_number


def mask_account_card(bank_info: str) -> str:
    """Функция маскировки номеров карт и номеров счетов"""
    formated_string = bank_info.split()
    if formated_string[0] == 'Счет' and len(formated_string[-1]) == 20:
        return f'{formated_string[0]} {get_mask_account(formated_string[1])}'
    elif formated_string[0] != 'Счет' and len(formated_string[-1]) == 16:
        type_card = ' '.join(formated_string[0:-1])
        return f'{type_card} {get_mask_card_number(formated_string[-1])}'
    else:
        raise ValueError('Некорректные данные (формат) номера карты (счета)')


def get_date(initial_date: str) -> str:
    """Функция, изменяющая формат даты"""
    if datetime.fromisoformat(initial_date):
        list_of_date = initial_date.split('T')
        formated_list = list_of_date[0].split('-')
        formated_date = '.'.join(formated_list[-1::-1])
        return formated_date
    else:
        raise ValueError('Некорректный формат (данные) даты')
