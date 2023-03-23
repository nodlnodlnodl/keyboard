"""
skoropis.png
"""

import re
import json


def main():
    cyrillic_lower_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя*.,?!-_\'()"'
    with open('text_2.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        text = text.lower()
    text = re.sub(r'[^а-я,*.?!\-_\'()"]', '', text)
    print(len(text))
    '''keys_dict = {1: '*', 2: '.', 3: 'ё', 4: 'ъ', 5: '?', 6: '!', 7: ' ', 8: '-', 9: '\'', 10: '(',
                 11: ')', 12: '_', 13: 'ц', 14: 'ь', 15: 'я', 16: ',', 17: '.', 18: 'з', 19: 'в', 20: 'к',
                 21: 'д', 22: 'ч', 23: 'ш', 24: 'щ', 25: '"', 26: 'у', 27: 'и', 28: 'е', 29: 'о', 30: 'а',
                 31: 'л', 32: 'н', 33: 'т', 34: 'с', 35: 'р', 36: 'й', 37: 'ф', 38: 'э', 39: 'х', 40: 'ы',
                 41: 'ю', 42: 'б', 43: 'м', 44: 'п', 45: 'г', 46: 'ж'}
'''

    fingers_dict = dict(f1={1: '*', 2: '.', 13: 'ц', 26: 'у', 37: 'ф'},
                        f2={3: 'ё', 14: 'ь', 27: 'и', 38: 'э'},
                        f3={4: 'ъ', 15: 'я', 28: 'е', 39: 'х'},
                        f4={5: '?', 6: '!', 16: ',', 17: '.', 29: 'о', 30: 'а', 40: 'ы', 41: 'ю'},
                        f5={7: ' ', 8: '-', 18: 'з', 19: 'в', 31: 'л', 32: 'н', 42: 'б', 43: 'м'},
                        f6={9: '\'', 20: 'к', 33: 'т', 44: 'п'},
                        f7={10: '(', 21: 'д', 34: 'с', 45: 'г'},
                        f8={11: ')', 12: '_', 22: 'ч', 23: 'ш', 24: 'щ', 25: '"', 35: 'р', 36: 'й', 46: 'ж'})

    temp = dict()
    for key, value in fingers_dict.items():
        for k, v in value.items():
            temp[v] = key

    with open("fingers_dict.json", "w", encoding='utf-8') as write_file:
        json.dump(temp, write_file)

    with open(r'fingers_dict.json', 'r', encoding='utf-8') as json_dict:
        data = json.load(json_dict)
        print(data)

    counter_fingers = {'f1': 0, 'f2': 0, 'f3': 0, 'f4': 0, 'f5': 0, 'f6': 0, 'f7': 0, 'f8': 0}
    for i in cyrillic_lower_letters:
        print(i, text.count(i))
        # print(data.get(i), text.count(i))
        for key, value in counter_fingers.items():
            if data.get(i) == key:
                counter_fingers[key] += text.count(i)
    print(counter_fingers)

    hand_dict = dict(left_hand={'f1': 0, 'f2': 0, 'f3': 0, 'f4': 0}, right_hand={'f5': 0, 'f6': 0, 'f7': 0, 'f8': 0})
    counter_hand = {'left_hand': 0, 'right_hand': 0}
    for key, value in counter_fingers.items():
        for k, v in hand_dict.items():
            if key in v:
                counter_hand[k] += value
    print(counter_hand)


if __name__ == '__main__':
    main()