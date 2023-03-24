import json
import re
import numpy


counter_fingers = {'f5l': 0, 'f4l': 0, 'f3l': 0, 'f2l': 0, 'f1l': 0, 'f1r': 0, 'f2r': 0, 'f3r': 0, 'f4r': 0, 'f5r': 0}


def create_dict():
    with open('diktor.json', encoding='utf-8') as kb_json:
        data_dict = json.load(kb_json)
    return data_dict


def get_cords(symbol):
    data_dict = create_dict()
    for key in data_dict:
        for value in data_dict[key]['key']:
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


def count_steps(first_sim, second_sim):
    if get_cords(first_sim)[1] - get_cords(second_sim)[1] == 0:
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