from utils import *
import pytest

"""
Андрей Архипкин - 100%
"""


@pytest.mark.parametrize("text, expected_result", [("у", 0),
                                                   ("Ё", 2),
                                                   ("1", 2),
                                                   ("йфя", 3)])
def test_count_steps_1(text, expected_result):
    text = re.sub(r'[^А-Яа-яёЁ1-9,*0.]', '', text)
    text = list(text)
    list_upper_case = [i for i in text if i.isupper()]
    value_passing_fingers(0, (len(list_upper_case) * 2))
    text = ''.join(text)
    text = [i.lower() for i in text]
    for i in range(1, len(text)):
        count_steps(text[i - 1], text[i])
    assert counter_fingers["f5l"] == expected_result


@pytest.mark.parametrize("text, expected_result", [("э", 0),
                                                   ("ИИИ", 0),
                                                   ("2", 0)])
def test_count_steps_2(text, expected_result):
    text = re.sub(r'[^А-Яа-яёЁ1-9,*0.]', '', text)
    text = list(text)
    list_upper_case = [i for i in text if i.isupper()]
    value_passing_fingers(0, (len(list_upper_case) * 2))
    text = ''.join(text)
    text = [i.lower() for i in text]
    for i in range(1, len(text)):
        count_steps(text[i - 1], text[i])
    assert counter_fingers["f4l"] == expected_result


@pytest.mark.parametrize("text, expected_result", [("я", 0),
                                                   ("ЭЭЭ", 0),
                                                   ("3", 0)])
def test_count_steps_3(text, expected_result):
    text = re.sub(r'[^А-Яа-яёЁ1-9,*0.]', '', text)
    text = list(text)
    list_upper_case = [i for i in text if i.isupper()]
    value_passing_fingers(0, (len(list_upper_case) * 2))
    text = ''.join(text)
    text = [i.lower() for i in text]
    for i in range(1, len(text)):
        count_steps(text[i - 1], text[i])
    assert counter_fingers["f3l"] == expected_result


@pytest.mark.parametrize("text, expected_result", [("ы", 0),
                                                   ("ООО", 0),
                                                   (",", 0),
                                                   ("4  ", 0)])
def test_count_steps_4(text, expected_result):
    text = re.sub(r'[^А-Яа-яёЁ1-9,*0.]', '', text)
    text = list(text)
    list_upper_case = [i for i in text if i.isupper()]
    value_passing_fingers(0, (len(list_upper_case) * 2))
    text = ''.join(text)
    text = [i.lower() for i in text]
    for i in range(1, len(text)):
        count_steps(text[i - 1], text[i])
    assert counter_fingers["f2l"] == expected_result