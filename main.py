from src.processing import filter_by_state, sort_by_date, process_bank_search
from src.reading_data_files import reading_csv, reading_excel
from src.generators import filter_by_currency
from src.utils import transactions_list
from src.widget import get_date, mask_account_card
import pandas as pd

print('Привет! Добро пожаловать в программу работы с банковскими транзакциями. Выберите необходимый пункт меню:\n'
      '1. Получить информацию о транзакциях из JSON-файла\n'
      '2. Получить информацию о транзакциях из CSV-файла\n'
      '3. Получить информацию о транзакциях из XLSX-файла\n')

choose_one = int(input())

if choose_one == 1:
    print('\nДля обработки выбран JSON-файл')
    processed_data = transactions_list('data/operations.json')
elif choose_one == 2:
    print('\nДля обработки выбран CSV-файл')
    processed_data = reading_csv('data/transactions.csv')
elif choose_one == 3:
    print('\nДля обработки выбран XLSX-файл')
    processed_data = reading_excel('data/transactions_excel.xlsx')

while True:
    print('\nВведите статус, по которому необходимо выполнить фильтрацию. '
          'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING: \n')
    choose_two = input()
    if choose_two.lower() in ['executed', 'canceled', 'pending']:
        filtred_data = filter_by_state(processed_data, choose_two)
        break
    else:
         print(f'\nСтатус операции {choose_two} недоступен')

while True:
    print('\nОтсортировать операции по дате? Да/Нет\n')
    choose_three = input()
    if choose_three.lower() == 'да':
        while True:
            print('\nОтсортировать по возрастанию или по убыванию?\n')
            choose_four = input()
            if choose_four.lower() == 'по возрастанию':
                sorted_data = sort_by_date(filtred_data, descending=False)
                break
            elif choose_four.lower() == 'по убыванию':
                sorted_data = sort_by_date(filtred_data)
                break
            else:
                print('\nНекорректный ввод направления сортировки')
        break
    elif choose_three.lower() == 'нет':
        sorted_data = filtred_data
        break
    else:
        print('\nНекорректный ввод сортировки')

while True:
    print('\nВыводить только рублевые транзакции? Да/Нет\n')
    choose_five = input()
    if choose_five.lower() == 'да':
        filtred_data_2 = list(filter_by_currency(sorted_data, 'RUB'))
        break
    elif choose_five.lower() == 'нет':
        filtred_data_2 = sorted_data
        break
    else:
        print('\nНекорректный ввод ответа')

while True:
    print('\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет\n')
    choose_six = input()
    if choose_six.lower() == 'да':
        print('\nВведите ключевое слово для поиска в описании операции:\n')
        choose_seven = input()
        filtred_data_3 = process_bank_search(filtred_data_2, choose_seven)
        if filtred_data_3 and (len(filtred_data_3[0]) == 7):
            print(f'\nРаспечатываю итоговый список транзакций...\n'
                  f'\nВсего банковских операций в выборке: {len(filtred_data_3)}\n')
            for item in filtred_data_3:
                if item['description'] == 'Открытие вклада':
                    print(f'{get_date(item['date'])} {item['description']}\n'
                          f'-> {mask_account_card(item['to'])}\n'
                          f'Сумма: {item['operationAmount']['amount']} {item['operationAmount']['currency']['name']}\n')
                else:
                    print(f'{get_date(item['date'])} {item['description']}\n'
                          f'{mask_account_card(item['from'])} -> {mask_account_card(item['to'])}\n'
                          f'Сумма: {item['operationAmount']['amount']} {item['operationAmount']['currency']['name']}\n')
            break
        elif filtred_data_3 and (len(filtred_data_3[0]) == 9):
            print(f'\nРаспечатываю итоговый список транзакций...\n'
                  f'\nВсего банковских операций в выборке: {len(filtred_data_3)}\n')
            for item in filtred_data_3:
                if item['description'] == 'Открытие вклада':
                    print(f'{get_date(item['date'])} {item['description']}\n'
                          f'-> {mask_account_card(item['to'])}\n'
                          f'Сумма: {item['amount']} {item['currency_name']}\n')
                else:
                    print(f'{get_date(item['date'])} {item['description']}\n'
                          f'{mask_account_card(item['from'])} -> {mask_account_card(item['to'])}\n'
                          f'Сумма: {item['amount']} {item['currency_name']}\n')
            break
        else:
            print(f'\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации')
            break

    elif choose_six.lower() == 'нет':
        if filtred_data_2 and (len(filtred_data_2[0]) == 7):
            print(f'\nРаспечатываю итоговый список транзакций...\n'
                  f'\nВсего банковских операций в выборке: {len(filtred_data_2)}\n')
            for item in filtred_data_2:
                if item['description'] == 'Открытие вклада':
                    print(f'{get_date(item['date'])} {item['description']}\n'
                          f'-> {mask_account_card(item['to'])}\n'
                          f'Сумма: {item['operationAmount']['amount']} {item['operationAmount']['currency']['name']}\n')
                else:
                    print(f'{get_date(item['date'])} {item['description']}\n'
                          f'{mask_account_card(item['from'])} -> {mask_account_card(item['to'])}\n'
                          f'Сумма: {item['operationAmount']['amount']} {item['operationAmount']['currency']['name']}\n')
            break
        elif filtred_data_2 and (len(filtred_data_2[0]) == 9):
            print(f'\nРаспечатываю итоговый список транзакций...\n'
                  f'\nВсего банковских операций в выборке: {len(filtred_data_2)}\n')
            for item in filtred_data_2:
                if item['description'] == 'Открытие вклада':
                    print(f'{get_date(item['date'])} {item['description']}\n'
                          f'-> {mask_account_card(item['to'])}\n'
                          f'Сумма: {item['amount']} {item['currency_name']}\n')
                else:
                    print(f'{get_date(item['date'])} {item['description']}\n'
                          f'{mask_account_card(item['from'])} -> {mask_account_card(item['to'])}\n'
                          f'Сумма: {item['amount']} {item['currency_name']}\n')
            break
        else:
            print(f'\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации')
            break
    else:
        print('\nНекорректный ввод ответа')
