# Импорт функций из src.utils
from src.utils import *

# Путь к файлу json
JSON_DATA_PATH = "../src/operations.json"


def main():

    # Поочередно вызываем функции обработки данных
    json_raw = get_json_data(JSON_DATA_PATH)
    clean_json = prepare_list(json_raw)
    sorted_json = sort_recs_by_date(clean_json)
    last_x_json = get_x_records(sorted_json)

    # В цикле обрабатываем списки данных и выводим на экран
    for x in last_x_json:
        data_rec_list = formatted_rec(x)
        list_date = formatted_date(data_rec_list)
        list_date_card = formatted_card(list_date)
        print_list = formatted_count(list_date_card)
        print(data_for_print(print_list))


# Вызов основной функции
main()
