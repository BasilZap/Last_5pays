from src import utils


def test_get_json_data():
    assert utils.get_json_data('tmp_dir/test.json') == [{"a": 1, "b": 2}]


def test_prepare_list():
    assert utils.prepare_list([{"a": 1, "b": 2}]) == []
    assert utils.prepare_list({}) == []
    assert utils.prepare_list([{'date': 1, 'from': 2, 'state': "EXECUTED"}]) == [
        {'date': 1, 'from': 2, 'state': "EXECUTED"}]


def test_sort_recs_by_date():
    assert utils.sort_recs_by_date([{'date': 1}, {'date': 3}, {'date': 2}]) == [
        {'date': 3}, {'date': 2}, {'date': 1}]
    assert utils.sort_recs_by_date([{'date': "2001-02-01"}, {'date': "2003-01-05"}]) == [
        {'date': "2003-01-05"}, {'date': "2001-02-01"}]


def test_get_x_records():
    assert utils.get_x_records([{'a': 1}, {'b': 3}, {'c': 2}, {'d': 1}, {'e': 3}, {'e': 5}]) == [
        {'a': 1}, {'b': 3}, {'c': 2}, {'d': 1}, {'e': 3}]
    assert utils.get_x_records([{'a': 1}, {'b': 3}]) == [{'a': 1}, {'b': 3}]
    assert utils.get_x_records([{'a': 1}, {'b': 3}], 1) == [{'a': 1}]
    assert utils.get_x_records([{'a': 1}, {'b': 3}], 4) == [{'a': 1}, {'b': 3}]


def test_formatted_rec():
    assert utils.formatted_rec({"date": "2019", "operationAmount": {"amount": "31",
                                "currency": {"name": "руб."}}, "description": "Перевод", "from": "Maestro",
                                "to": "Счет"}) == ['2019', 'Перевод', 'Maestro', 'Счет', '31', 'руб.']


def test_formatted_date():
    assert utils.formatted_date(['2019-11-10']) == ['10.11.2019']
    assert utils.formatted_date(['2019-08-26T10:50:58.294041']) == ['26.08.2019']


def test_formatted_card():
    assert utils.formatted_card(['', '', 'Maestro 1596837868705199']) == ['', '', 'Maestro 1596 83** **** 5199']
    assert utils.formatted_card(['', '', 'Счет 75106830613657916952']) == ['', '', 'Счет **6952']


def test_formatted_count():
    assert utils.formatted_count(['', '', '', 'Счет 75106830613657916952']) == ['', '', '', 'Счет **6952']


def test_data_for_print():
    assert utils.data_for_print(['2019', 'Перевод', 'Maestro', 'Счет', '31', 'руб.']) == '\n2019 Перевод\nMaestro -> ' \
                                                                                         'Счет\n31 руб.'
