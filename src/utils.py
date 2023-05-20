import json
from datetime import date

JSON_DATA_PATH = "../src/operations.json"

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
    отсеивание нестандартных операций
    :param raw_json:
    :return:
    """
    normalized_j_list = []
    key_date = 'date'
    key_from = 'from'
    for j_rec in raw_json:
        if type(j_rec) is dict:
            if dict(j_rec).get(key_date) and dict(j_rec).get(key_from):
                normalized_j_list.append(j_rec)
    return normalized_j_list


def sort_recs_by_date(raw_json):
    """
    Сортировка данных по дате
    и времени по убыванию
    :param raw_json: нормализованный список
    :return: сортированный список
    """
    operation_date_time = sorted(raw_json, key=lambda x: (x['date']), reverse=True)
    return operation_date_time


def formatted_date(json_rec):
    j_rec = dict(json_rec)
    # форматируем дату для вывода
    transact_date = str(j_rec['date']).partition('T')[0]
    non_form_date = date.fromisoformat(transact_date)
    form_date = non_form_date.strftime("%d-%m-%Y")

    # форматируем данные карты для вывода
    card_list = str.split(j_rec["from"])
    card_num = card_list[-1]
    num_hide = card_num[:6] + (len(card_num[6:-4]) * '*') + card_num[-4:]
    num_form = num_hide[:4] + " " + num_hide[4:8] + " " + num_hide[8:12] + " " + num_hide[12:]
    card_list[-1] = num_form

    # форматируем номер счета для вывода
    transaction_list = str.split(j_rec["to"])
    transaction_num = transaction_list[-1]
    transaction_list[-1] = "**" + transaction_num[-4:]

    # формируем строку для вывода
    text_record = (f"{form_date} {j_rec['description']}\n"
                   f"{' '.join(card_list)} -> {' '.join(transaction_list)}\n"
                   f"{j_rec['operationAmount']['amount']} "
                   f"{j_rec['operationAmount']['currency']['name']}\n")
    return text_record


def print_data():
    pass


x = sort_recs_by_date(prepare_list(get_json_data(JSON_DATA_PATH)))
print(formatted_date(x[0]))
