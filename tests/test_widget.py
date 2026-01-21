import pytest
from masks import get_mask_account, get_mask_card_number
from widget import mask_account_card, get_date

@pytest.mark.parametrize ('bank_data, masked_data', zip(
    ['Maestro 1596837868705199', 'Счет 64686473678894779589', 'Visa Classic 6831982476737658' ],
    ['Maestro 1596 83** **** 5199 ', 'Счет **9589', 'Visa Classic 6831 98** **** 7658 ']))
def test_mask_account_card(bank_data, masked_data):
    assert mask_account_card(bank_data) == masked_data


@pytest.fixture(params = ['Maestro 159683786870519923', #тестируем длинный номер карты
            'Счет 64686473678894',                      #тестируем короткий номер счета
            'Visa Classic ',                            #тестируем пустой номер карты
            'Счет ',                                    #тестируем пустой номер счета
            'Master Card 12345678'])                    #тестируем короткий номер карты
def bank_datas(request):
    return request.param

def test_mask_account_card_incorrect(bank_datas):
    with pytest.raises(ValueError):
        mask_account_card(bank_datas)

@pytest.mark.parametrize ('init_data, correct_data', zip(
    ['2024-03-11T02:26:18.671407', '2025-12-20T12:21:48.683407', '1988-07-31T23:59:59.999999' ],
    ['11.03.2024', '20.12.2025', '31.07.1988']))
def test_get_date(init_data, correct_data):
    assert get_date(init_data) == correct_data

@pytest.fixture(params = ['2024-02-30T02:58:18.671407', #тестируем некорректное число месяца
            '2024-14-30T02:58:18.671407',               #тестируем некорректный месяц
            '202-10-30T02:58:18.671407',                #тестируем некорректный формат года (должно быть 4 символа)
            '2024-10-30T25:58:18.671407',               #тестируем некорректный час
            '2024-10-30T05:78:18.671407',               #тестируем некорректные минуты
            '2024-10-30T05:58:88.671407',               #тестируем некорректные секунды
            '31.07.1988']    )                          #тестируем некорректный формат даты
def list_dates(request):
    return request.param

def test_get_date_incorrect(list_dates):
    with pytest.raises(ValueError):
        get_date(list_dates)




