import json


def get_json_data():
    """
    Чтение файла json
    :return: список операций
    """
    with open("operations.json", "r", encoding="utf-8") as json_file:
        raw_json = json.loads(json_file.read())
    return raw_json


def prepare_list(raw_json):
    """
    Нормализация данных полученных из json:
    отсеивание нестандартных операций
    :param raw_json:
    :return:
    """
    normalized_j_list = []
    key_date = 'date'
    key_from = 'from'
    for j_rec in raw_json:
        if dict(j_rec).get(key_date) and dict(j_rec).get(key_from):
            normalized_j_list.append(j_rec)
    return normalized_j_list


def make_sorted_ops(raw_json):
    """
    Сортировка данных по дате
    и времени по убыванию
    :param raw_json: нормализованный список
    :return: сортированный список
    """
    operation_date_time = sorted(raw_json, key=lambda x: (x['date']), reverse=True)
    return operation_date_time


def formatted_data():
    pass


def print_data():
    pass



print(make_sorted_ops(prepare_list(get_json_data())))

