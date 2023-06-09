# Анализ удобства раскладки

##   

Для установки модулей используйте `pip install -r requirements.txt`

Для запуска программы используйте `python main.py`

#

Ходят 'слухи', что йцукен ~~зажиток пендосов 19 века~~ неудобная раскладка для написания различных текстов.

Мы решили выяснить действительно ли йцукен малоэффективная раскладка. Сравнивать её мы будем с раскладкой диктор.

Программа посчитает нагрузку на каждый палец при использовании раскладок:

* йцукен
* диктор

**Нумерация клавиш**

![раскладка](https://sun1-24.userapi.com/impg/J9-yxGznQEUdR4_FQGFx62Wn1g_R3vmK3eAr9g/Thd0O5aaJyw.jpg?size=826x251&quality=96&sign=ca66b193e8d7b76a8ae6395dcc858d46&type=album)

**Раскладка йцукен**

![раскладка йцукен](https://hsto.org/r/w1560/getpro/geektimes/post_images/766/a78/9eb/766a789eb2a7bf3e024bbf0602d53d87.png)

**Раскладка диктор**

![раскладка диктор](https://hsto.org/r/w1560/getpro/geektimes/post_images/dd7/793/5e6/dd77935e6b65b5b49aad609da43157db.jpg)

Рассммотрим как будет оптимально нагружать пальцы каждая из раскладок

#### Оптимальность достигается за счет сравнения попальцевых нагрузок (вектор-путь каждого пальца каждой руки при 10-пальцевом вводе при слепой печати) ####

#

На вход программе подается текст, он разбивается на строки, каждая строка разбивается на слова, после каждого слова наши
пальчики возвращаются на хоум ряд и так циклим до конца текста.

С помощью не хитрых манипуляций считаем нагрузку на все пальчики.
Затем в принте выводим результат для двух раскладок и можем зрительно сравнить какая из раскладок удобнее для печати
разных текстов

# Итого что имеем?

Вывод программы:

| ДИКТОР                | ЙЦУКЕН |
|-----------------------|--------|
| f1l - 1822  f1r - 1490 <br/>f2l - 2251	f2r - 3366<br/>f3l - 526	f3r - 1113<br/>f4l - 471	f4r - 936<br/>f5l - 673	f5r - 1196| f1l - 1987	f1r - 1325<br/>f2l - 7813	f2r - 6245<br/>f3l - 1733	f3r - 545<br/>f4l - 559	f4r - 175<br/>f5l - 1208	f5r - 815|
|13844|22405|

Во-первых, у раскладки диктор нагрузка в 1.6 раз меньше.

Во-вторых, в раскладке диктор нагрузка на пальцы +- равномерна, в отличии от йцукен

**Итого:**

Каждый юзает раскладку на свой лад, но мы подтвердили 'слух' о том, что йцукен ~~зажиток пендосов 19 века~~ хуже по
нагрузке, сравнив её с раскладкой диктор

:shipit:






























