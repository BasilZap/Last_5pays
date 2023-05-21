# Программа вывода пяти последних удачных платежных операций!

Функции:
get_json_data(path) - Считывает данные json из файла
prepare_list(raw_json) - Подготовка данных, если нет интересующих записей - отсеиваем
sort_recs_by_date(raw_json) - Сортируем список по дате операции
get_x_records(raw_json, x=5) - Получение x последних операций (5 по умолчанию)
formatted_rec(raw_json) - Создает список с необходимыми данными
formatted_date(rec_date) - Форматируем данные о дате транзакции, возвращаем (f_rec_date)
formatted_card(rec_card) - Форматируем данные карты, возвращаем (f_rec_card)
formatted_count(rec_count) - Форматируем данные счета, возвращаем (f_rec_count)
data_for_print(f_rec_date, f_rec_card, f_rec_count) - Формируем данные для печати
