import pytest
from processing import filter_by_state, sort_by_date


@pytest.fixture
def dic_list():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


@pytest.fixture
def filtred_dics():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


def test_filter_by_state_1(dic_list, filtred_dics):      # тестирование функции filter_by_state со
    assert filter_by_state(dic_list) == filtred_dics     # значением 'state' по умолчанию


@pytest.fixture
def filtred_dics_2():
    return [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def test_filter_by_state_2(dic_list, filtred_dics_2):                    # тестирование функции filter_by_state
    assert filter_by_state(dic_list, 'CANCELED') == filtred_dics_2  # со значением 'state' == 'CANCELED'


def test_filter_by_state_unknown_state(dic_list):       # тестирование функции filter_by_state
    with pytest.raises(ValueError):                     # с несуществующим значением 'state'
        filter_by_state(dic_list, 'PROCESSING')


@pytest.fixture
def sorted_by_date_1():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


def test_sort_by_date_1(dic_list, sorted_by_date_1):   # тестирование сортировки словарей по убыванию
    assert sort_by_date(dic_list) == sorted_by_date_1


@pytest.fixture
def dic_list_2():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-06-30T08:21:33.419441'}]


@pytest.fixture
def sorted_by_date_2():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-06-30T08:21:33.419441'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


def test_sort_by_date_2(dic_list_2, sorted_by_date_2):   # тестирование сортировки словарей с одинаковыми датами
    assert sort_by_date(dic_list_2) == sorted_by_date_2


@pytest.fixture
def sorted_by_date_3():
    return [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]


def test_sort_by_date_3(dic_list, sorted_by_date_3):   # тестирование сортировки словарей по возрастанию
    assert sort_by_date(dic_list, False) == sorted_by_date_3


@pytest.fixture
def dic_list_3():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-15-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-06-30T08:21:33.419441'}]


def test_sort_by_date_incorrect_1(dic_list_3):       # тестирование сортировки с некорректным месяцем
    with pytest.raises(ValueError):
        sort_by_date(dic_list_3)


@pytest.fixture
def dic_list_4():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '26.01.2017'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-06-30T08:21:33.419441'}]


def test_sort_by_date_incorrect_2(dic_list_4):       # тестирование сортировки с некорректным форматом даты
    with pytest.raises(ValueError):
        sort_by_date(dic_list_4, False)
