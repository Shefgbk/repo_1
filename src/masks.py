import logging
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

rel_file_path = os.path.join(current_dir, "../logs/masks.log")
abs_file_path = os.path.abspath(rel_file_path)

logger = logging.getLogger('masks')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(abs_file_path, 'w', encoding="utf-8")
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """ Функция, возвращающая маску номера карты клиента """
    logger.info('Ввод номера карты клиента')
    if len(card_number) == 16 and card_number.isdigit():
        changed_string = '******'.join([card_number[:6], card_number[12:]])
        masked_card = ''
        for i in range(0, 15, 4):
            masked_card += changed_string[i: i + 4] + ' '
        logger.info('Вывод маски номера карты')
        return masked_card
    elif card_number.isalpha():
        logger.error('Введенный номер карты содержит буквы')
        raise ValueError('Номер карты должен состоять из цифр')
    else:
        logger.error('Некорректный формат/длина номера карты')
        raise ValueError('Некорректная длина (формат) номера карты')


def get_mask_account(bank_account: str) -> str:
    """Функция, возвращающая маску номера счета клиента"""
    logger.info('Ввод номера счета клиента')
    if len(bank_account) == 20 and bank_account.isdigit():
        masked_account = '**' + bank_account[-4:]
        logger.info('Вывод маски номера счета')
        return masked_account
    elif bank_account.isalpha():
        logger.error('Введенный номер счета содержит буквы')
        raise ValueError('Номер счета должен состоять из цифр')
    else:
        logger.error('Некорректный формат/длина счета карты')
        raise ValueError('Некорректная длина (формат) номера счета')
