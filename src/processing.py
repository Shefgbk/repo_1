from datetime import datetime


def filter_by_state(dic_list: list, state: str = 'EXECUTED') -> list:
    """ Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state (по умолчанию 'EXECUTED') соответствует указанному значению """
    filtred_dic_list = []
    for dic in dic_list:
        if dic['state'] == state:
            filtred_dic_list.append(dic)
    return filtred_dic_list


def sort_by_date(dict_list: list, descending: bool = True) -> list:
    """ Функция возвращает новый список словарей,
    отсортированных по дате (по умолчанию — убывание) """
    sorted_list = sorted(dict_list, key=lambda x: datetime.fromisoformat(x['date']), reverse=descending)
    return sorted_list
