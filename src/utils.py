import json
from datetime import date


def get_json_data(data_path):
    """
    Чтение файла json
    :return: список операций
    """
    with open(data_path, "r", encoding="utf-8") as json_file:
        raw_json = json.loads(json_file.read())
    return raw_json


def prepare_list(raw_json):
    """
    Нормализация данных полученных из json:
    отсеивание нестандартных элементов списка и операций
    :param raw_json:
    :return: Список библиотек normalized_j_list
    """
    normalized_j_list = []
    key_date = 'date'
    key_from = 'from'
    key_exec = 'state'
    for j_rec in raw_json:
        if type(j_rec) is dict:
            if dict(j_rec).get(key_date) and dict(j_rec).get(key_from):
                if dict(j_rec).get(key_exec) == "EXECUTED":
                    normalized_j_list.append(j_rec)
    return normalized_j_list


def sort_recs_by_date(raw_json):
    """
    Сортировка данных по дате
    и времени по убыванию
    :param raw_json: нормализованный список
    :return: сортированный список библиотек operation_date_time
    """
    operation_date_time = sorted(raw_json, key=lambda x: (x['date']), reverse=True)
    return operation_date_time


def get_x_records(raw_json, x=5):
    """
    Принимает сортированный список библиотек
    возвращает первые x элементов
    :param raw_json: сортированный список библиотек
    :param x: Количество элементов для вывода
    :return: Список из x элементов
    """
    rec_list = []
    for rec in range(x):
        rec_list.append(raw_json[rec])
    return rec_list


def formatted_rec(raw_json):
    """
    Формирует список необходимых
    для вывода значений
    :param raw_json: Список элементов в формате json
    :return: Список элементов в формате string
    """
    data_list = [raw_json['date'], raw_json['description'], raw_json['from'], raw_json['to'],
                 raw_json["operationAmount"]["amount"], raw_json["operationAmount"]["currency"]["name"]]
    return data_list


def formatted_date(data_list):
    """
    Форматирует дату для вывода
    :param data_list: список значений для вывода
    :return: список значений для вывода
    """
    transact_date = str(data_list[0]).partition('T')[0]
    non_form_date = date.fromisoformat(transact_date)
    data_list[0] = non_form_date.strftime("%d-%m-%Y")
    return data_list


def formatted_card(data_list):
    """
    Форматирует данные карты для вывода
    :param data_list: список значений для вывода
    :return: список значений для вывода
    """
    card_list = str.split(data_list[2])
    card_num = card_list[-1]
    num_hide = card_num[:6] + (len(card_num[6:-4]) * '*') + card_num[-4:]
    num_form = num_hide[:4] + " " + num_hide[4:8] + " " + num_hide[8:12] + " " + num_hide[12:]
    card_list[-1] = num_form
    data_list[2] = ' '.join(card_list)
    return data_list


def formatted_count(data_list):
    """
    Форматирует номер счета для вывода
    :param data_list: список значений для вывода
    :return: список значений для вывода
    """
    transaction_list = str.split(data_list[3])
    transaction_num = transaction_list[-1]
    transaction_list[-1] = "**" + transaction_num[-4:]
    data_list[3] = ' '.join(transaction_list)
    return data_list


def data_for_print(data_list):
    """
    Форматирует строку для вывода на экран
    :param data_list:
    :return:
    """
    f_rec_date, desc, f_rec_card, f_rec_count, amount, name = data_list
    text_record = (f"\n{f_rec_date} {desc}\n"
                   f"{f_rec_card} -> {f_rec_count}\n"
                   f"{amount} {name}")
    return text_record
