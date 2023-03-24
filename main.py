#!/usr/bin/python
# -*- coding: utf-8 -*-
# pip install -r requirements.txt
from utils import *


if __name__ == "__main__":
    with open('text.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    text = re.sub(r'[^А-Яа-яёЁ1-9,*0.]', '', text)
    text = list(text)
    list_upper_case = [i for i in text if i.isupper()]
    value_passing_fingers(0, (len(list_upper_case) * 2))
    text = ''.join(text)
    text = [i.lower() for i in text]
    print(text)
    for i in range(1, len(text)):
        count_steps(text[i - 1], text[i])
    print(counter_fingers)