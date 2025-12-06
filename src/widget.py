from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(bank_info: str) -> str:
    """Функция маскировки номеров карт и номеров счетов"""
    formated_string = bank_info.split()
    if formated_string[0] == "Счет":
        return f'{formated_string[0]} {get_mask_account(formated_string[1])}'
    else:
        type_card = " ".join(formated_string[0:-1])
        return f'{type_card} {get_mask_card_number(formated_string[-1])}'

