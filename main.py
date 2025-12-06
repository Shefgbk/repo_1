#from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card

#print(get_mask_card_number("7000792289606361"))
#print(get_mask_account("73654108430135874305"))
print(mask_account_card('Maestro 1596837868705199'))
print(mask_account_card('Счет 64686473678894779589'))
print(mask_account_card('Visa Classic 6831982476737658'))
