from src.processing import process_bank_operations, filter_by_state, sort_by_date
from src.reading_data_files import reading_csv, reading_excel
from src.generators import filter_by_currency
from src.utils import transactions_list

print('Привет! Добро пожаловать в программу работы с банковскими транзакциями. Выберите необходимый пункт меню:\n'
      '1. Получить информацию о транзакциях из JSON-файла\n'
      '2. Получить информацию о транзакциях из CSV-файла\n'
      '3. Получить информацию о транзакциях из XLSX-файла')
choose_one = int(input())
if choose_one == 1:
    print('Для обработки выбран JSON-файл')
    processed_data = list(transactions_list('data/operations.json'))
while True:
    print('Введите статус, по которому необходимо выполнить фильтрацию. '
          'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING: ')
    choose_two = input()
    if choose_two.lower() in ['executed', 'canceled', 'pending']:
        filtred_data = filter_by_state(processed_data, choose_two)
        break
    else:
         print(f'Статус операции {choose_two} недоступен\n')
while True:
    print('Отсортировать операции по дате? Да/Нет')
    choose_three = input()
    if choose_three.lower() == 'да':
        while True:
            print('Отсортировать по возрастанию или по убыванию?')
            choose_four = input()
            if choose_four.lower() == 'по возрастанию':
                sorted_data = sort_by_date(filtred_data, descending=False)
                break
            elif choose_four.lower() == 'по убыванию':
                sorted_data = sort_by_date(filtred_data)
                break
            else:
                print('Некорректный ввод направления сортировки')
        break
    elif choose_three.lower() == 'нет':
        sorted_data = filtred_data
        break
    else:
        print('Некорректный ввод сортировки')
while True:
    print('Выводить только рублевые транзакции? Да/Нет')
    choose_five = input()
    if choose_five.lower() == 'да':
        filtred_data_2 = list(filter_by_currency(sorted_data, 'RUB'))
        break
    elif choose_five.lower() == 'нет':
        filtred_data_2 = sorted_data
        break
    else:
        print('Некорректный ввод ответа')
