def get_mask_card_number(card_number: str) -> str:
    """Функция, возвращающая маску номера карты клиента"""
    if len(card_number) == 16 and card_number.isdigit():
        changed_string = '******'.join([card_number[:6], card_number[12:]])
        masked_card = ''
        for i in range(0, 15, 4):
            masked_card += changed_string[i: i + 4] + ' '
        return masked_card
    elif card_number.isalpha():
        raise ValueError('Номер карты должен состоять из цифр')
    else:
        raise ValueError('Некорректная длина (формат) номера карты')


def get_mask_account(bank_account: str) -> str:
    """Функция, возвращающая маску номера счета клиента"""
    if len(bank_account) == 20 and bank_account.isdigit():
        masked_account = '**' + bank_account[-4:]
        return masked_account
    elif bank_account.isalpha():
        raise ValueError('Номер счета должен состоять из цифр')
    else:
        raise ValueError('Некорректная длина (формат) номера счета')

