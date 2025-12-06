def get_mask_card_number(card_number: str) -> str:
    """Функция, возвращающая маску номера карты клиента"""
    changed_string = "******".join([card_number[:6], card_number[12:]])
    masked_card = ""
    for i in range(0, 15, 4):
        masked_card += changed_string[i: i + 4] + " "
    return masked_card


def get_mask_account(bank_account: str) -> str:
    """Функция, возвращающая маску номера счета клиента"""
    masked_account = "**" + bank_account[-4:]
    return masked_account
