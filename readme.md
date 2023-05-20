Программа вывода пяти последних удачных платежных операций!

Функции:
get_json_data(path) Считывает данные json из файла
prepare_list(raw_json) Подготовка данных, если нет интересующих записей - отсеиваем
make_sorted_ops(raw_json) Сортируем список по дате операции
get_x_records(raw_json, x=5) получение x последних операций (5 по умолчанию)
formatted_date(rec_date) форматируем данные о дате транзакции, возвращаем (f_rec_date)
formatted_card(rec_card) форматируем данные карты, возвращаем (f_rec_card)
formatted_count(rec_count) форматируем данные счета, возвращаем (f_rec_count)
data_for_print(f_rec_date, f_rec_card, f_rec_count) формируем данные для печати
