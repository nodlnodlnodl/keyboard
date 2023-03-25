import json
import re
from diktor import *


def get_cords(symbol):
    """
     На ход ноги получаем символ,
     на выход список из ряда и колоны
    """
    for key in data_dict:
        for value in data_dict[key]['key']:
            if value == symbol:
                return [data_dict[key]['raw'], data_dict[key]['column']]


def get_cords_qwer(symbol):
    """
     На ход ноги получаем символ,
     на выход список из ряда и колоны
    """
    for key in data_dict:
        for value in data_dict[key]['qwer']:
            if value == symbol:
                return [data_dict[key]['raw'], data_dict[key]['column']]


def value_passing_fingers(column, value):
    match column:
        case 0 | 1:
            counter_fingers['f5l'] += value
        case 2:
            counter_fingers['f4l'] += value
        case 3:
            counter_fingers['f3l'] += value
        case 4 | 5:
            counter_fingers['f2l'] += value
        case 6 | 7:
            counter_fingers['f2r'] += value
        case 8:
            counter_fingers['f3r'] += value
        case 9:
            counter_fingers['f4r'] += value
        case 10 | 11 | 12:
            counter_fingers['f5r'] += value


def value_passing_fingers_qwer(column, value):
    """
    нахера две аналогичные функции, так-то работает ничего не изменится
    но сделай покрасоте умоляю
    """
    match column:
        case 0 | 1:
            counter_fingers_qwer['f5l'] += value
        case 2:
            counter_fingers_qwer['f4l'] += value
        case 3:
            counter_fingers_qwer['f3l'] += value
        case 4 | 5:
            counter_fingers_qwer['f2l'] += value
        case 6 | 7:
            counter_fingers_qwer['f2r'] += value
        case 8:
            counter_fingers_qwer['f3r'] += value
        case 9:
            counter_fingers_qwer['f4r'] += value
        case 10 | 11 | 12:
            counter_fingers_qwer['f5r'] += value


def count_steps(first_sim, second_sim):
    if get_cords(first_sim)[1] == get_cords(second_sim)[1]:
        value_passing_fingers(get_cords(second_sim)[1], abs(get_cords(first_sim)[0] - get_cords(second_sim)[0]))
    else:
        if get_cords(first_sim)[0] != get_cords(second_sim)[0]:
            match get_cords(second_sim)[1]:
                case 5 | 6:
                    if get_cords(second_sim)[0] == 2:
                        value_passing_fingers(get_cords(second_sim)[1], 1)
                    else:
                        value_passing_fingers(get_cords(second_sim)[1],
                                              abs(get_cords(first_sim)[0] - get_cords(second_sim)[0]) + 1)
                case 1 | 2 | 3 | 4 | 7 | 8 | 9 | 10:
                    if get_cords(second_sim)[0] == 2:
                        pass
                    else:
                        value_passing_fingers(get_cords(second_sim)[1],
                                              abs(get_cords(first_sim)[0] - get_cords(second_sim)[0]))
                case 11:
                    value_passing_fingers(get_cords(second_sim)[1],
                                          abs(get_cords(first_sim)[0] - get_cords(second_sim)[0]) + 1)
                case 12:
                    value_passing_fingers(get_cords(second_sim)[1],
                                          abs(get_cords(first_sim)[0] - get_cords(second_sim)[0]) + 2)
        if get_cords(first_sim)[0] == get_cords(second_sim)[0]:
            match get_cords(second_sim)[1]:
                case 5 | 6 | 11:
                    value_passing_fingers(get_cords(second_sim)[1],
                                          abs(get_cords(second_sim)[0] - 2) + 1)
                case 1 | 2 | 3 | 4 | 7 | 8 | 9 | 10:
                    value_passing_fingers(get_cords(second_sim)[1],
                                          abs(get_cords(second_sim)[0] - 2))
                case 12:
                    value_passing_fingers(get_cords(second_sim)[1],
                                          abs(get_cords(second_sim)[0] - 2) + 2)


def count_spaces(text):
    text = re.sub(r'[^" "]', '', text)
    counter_fingers_qwer['f1l'] += int(len(text) * 0.6)
    counter_fingers_qwer['f1r'] += int(len(text) * 0.4)
    counter_fingers['f1l'] += int(len(text) * 0.55)
    counter_fingers['f1r'] += int(len(text) * 0.45)


def count_steps_qwer(first_sim, second_sim):
    """
    Интегрируйте эту херь в предыдущую функцию
    на кой хер тут две аналогичные функции
    """
    if get_cords_qwer(first_sim)[1] == get_cords_qwer(second_sim)[1]:
        value_passing_fingers_qwer(get_cords_qwer(second_sim)[1], abs(get_cords_qwer(first_sim)[0] - get_cords_qwer(second_sim)[0]))
    else:
        if get_cords_qwer(first_sim)[0] != get_cords_qwer(second_sim)[0]:
            match get_cords_qwer(second_sim)[1]:
                case 5 | 6:
                    if get_cords_qwer(second_sim)[0] == 2:
                        value_passing_fingers_qwer(get_cords_qwer(second_sim)[1], 1)
                    else:
                        value_passing_fingers_qwer(get_cords_qwer(second_sim)[1],
                                              abs(get_cords_qwer(first_sim)[0] - get_cords_qwer(second_sim)[0]) + 1)
                case 1 | 2 | 3 | 4 | 7 | 8 | 9 | 10:
                    if get_cords_qwer(second_sim)[0] == 2:
                        pass
                    else:
                        value_passing_fingers_qwer(get_cords_qwer(second_sim)[1],
                                              abs(get_cords_qwer(first_sim)[0] - get_cords_qwer(second_sim)[0]))
                case 11:
                    value_passing_fingers_qwer(get_cords_qwer(second_sim)[1],
                                          abs(get_cords_qwer(first_sim)[0] - get_cords_qwer(second_sim)[0]) + 1)
                case 12:
                    value_passing_fingers_qwer(get_cords_qwer(second_sim)[1],
                                          abs(get_cords_qwer(first_sim)[0] - get_cords_qwer(second_sim)[0]) + 2)
        if get_cords_qwer(first_sim)[0] == get_cords_qwer(second_sim)[0]:
            match get_cords_qwer(second_sim)[1]:
                case 5 | 6 | 11:
                    value_passing_fingers_qwer(get_cords_qwer(second_sim)[1],
                                          abs(get_cords_qwer(second_sim)[0] - 2) + 1)
                case 1 | 2 | 3 | 4 | 7 | 8 | 9 | 10:
                    value_passing_fingers_qwer(get_cords_qwer(second_sim)[1],
                                          abs(get_cords_qwer(second_sim)[0] - 2))
                case 12:
                    value_passing_fingers_qwer(get_cords_qwer(second_sim)[1],
                                          abs(get_cords_qwer(second_sim)[0] - 2) + 2)


def print_fingers():
    print(f'\t\tDIKTOR\t\t\t\t\t\t\tQWERTY')
    print(f'f1l - {counter_fingers["f1l"]}\tf1r - {counter_fingers["f1r"]}\t\t\tf1l - {counter_fingers_qwer["f1l"]}\tf1r - {counter_fingers_qwer["f1r"]}')
    print(f'f2l - {counter_fingers["f2l"]}\tf2r - {counter_fingers["f2r"]}\t\t\tf2l - {counter_fingers_qwer["f2l"]}\tf2r - {counter_fingers_qwer["f2r"]}')
    print(f'f3l - {counter_fingers["f3l"]}\tf3r - {counter_fingers["f3r"]}\t\t\tf3l - {counter_fingers_qwer["f3l"]}\tf3r - {counter_fingers_qwer["f3r"]}')
    print(f'f4l - {counter_fingers["f4l"]}\tf4r - {counter_fingers["f4r"]}\t\t\tf4l - {counter_fingers_qwer["f4l"]}\tf4r - {counter_fingers_qwer["f4r"]}')
    print(f'f5l - {counter_fingers["f5l"]}\tf5r - {counter_fingers["f5r"]}\t\t\tf5l - {counter_fingers_qwer["f5l"]}\tf5r - {counter_fingers_qwer["f5r"]}')
