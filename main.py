# Регулярные выражения (поиск по паттерну)
# Regular expressions (re)
# r-строка - raw-string ("сырая" строка) - отключение всех управляющих символов
# Квантификаторы (quantity)
# {m} - ровно m раз
# {m,}- m раз и более
# {n,} - не более n раз
# {m,n} - от m до n (без пробела)
# ? - от нуля до одного (аналог {0,1})
# * - от нуля до бесконечности (32767) {0,}
# + - от 1 до бесконечности (32767) {1,}
import re
import requests

pattern = r'<img[^>]+src="([^">]+)"'
# test_string = 'img height="50" width="150" src="images/bg.jpg"'
html = requests.get('https://yandex.ru').text
result = re.findall(pattern, html)
print(result)

# pattern = r'\b\w{4}\b' # все слова из 4 символов
# pattern = r'\d'
# pattern = r'd{3}' # три цифры подряд
# pattern = r'начало!\Z' # строка заканчивается на "начало!"
# pattern = '[0-5][0-9]' # последовательность из двух цифр
# pattern = '[а-яА-я]'  # все буквы от а до я и от А до Я
# pattern = '[^ерм]' # Исключить символы: [ерм]
# pattern = r'\((.+?)\)' # вытащить текст из скобок
# pattern = 'o{2,5}' # Вывести "о" которое встречается от 2 до 5 раз
# pattern = 'Go{2,}gle'

# pattern = r'стеклянн?ый' # 2-я "н" может присутствовать
# "жадный" квантификатор (greedy quantifier)

# pattern = r'<img.*>' # жадный(greedy) квантификатор
# pattern = r'<img.*?>' # ленивый(lazy, non-greedy) квантификатор
# pattern = r'<img[^>]+src="([^">]+)"' # только путь к картинке
# pattern = r'<p>(.*?)</p>' # содержимое абзаца html
# pattern = r'p[^>]*>(.*)</p>' # содержимое абзаца html c атрибутами
# result = re.findall(pattern, test_string)

# print('Цифры есть.') if result else print('Цифр нет.') # тернарный if (тернарный условный оператор) (три конца и никаких elif)

# Убираем все знаки препинания
# def remove_punctuation(input_str: str) -> str:
#     """
#     Методом sub() заменяем все найденные совпадения
#     пустой строкой и возвращаем "очищенную"
#     :param input_str: строка со знаками препинания
#     :return: строку, очищенную от знаков препинания
#     """
#     return re.sub(r'[^\w\s]','',input_str)
# test_string = ('Для 1 000 знаков текста подходят стр??????????аницы приветственных текстов,'
#                ' описания больших карточек товаров, рекламные посты, короткие письма для рассылки,'
#                ' малые тексты “О компании” и другие подобные форматы.')
#
# pattern = r'[,.;:!]'
# test_string = 'яблоко,           груша.      банан;          слива!абрикос'
# # test_string = ''.join(test_string.split()) # убрали все пробелы
# result = re.split(pattern, test_string) # убираем знаки по паттерну
#
# # через map
# # result = list(map(lambda x: x.strip(), result))
#
# # через list comprehension с сортировкой
# result = sorted(x.strip() for x in result)
# print(result)




# Линтеры - статический анализатор кода (контролирует следование хорошим практикам)
# Flake8 - самый популярный линтер
# pip install flake8
# (flake8-bugbear - для нахождения распространенных логических ошибок в коде)
# (pep8-naming - проверяет имена на соответствие pep8)
# pip install flake8-bugbear pep8-naming
# Arguments: --max-complexity 10 $FileDir$/$FileName$
# Path: $FileDir$
# Advanced Options/OutputFilter: $FILE_PATH$:$LINES$

# Библиотека pymorphy
# pip install pymorphy3
# pip install -U pymorphy3-dicts-ru
# import pymorphy3
#
# form = pymorphy3.MorphAnalyzer().parse('бутылка')[0]
#
# for btl in reversed(range(99)):
#     print(f'В холодильнике {btl + 1} {form.make_agree_with_number(btl+1).word} пива')
#     print('Возьмем одну и выпьем.')
#     if btl % 10 == 1 and btl != 11:
#         remain = 'Осталась'
#     else:
#         remain = 'Осталось'
#     print(f'{remain} {btl} {form.make_agree_with_number(btl).word} пива.')

# Исключения (runtime)
# try:
#   что пытаемся сделать
# except:
#   обрабатываем исключения
# else:
#   если исключения не было
# finally:
#   выполняется в любом случае


# # Практикум (обучаемый словарь)
# import pickle
#
# # Минимальная версия, если файл dict.dat отсутствует
# voc = {
#     'стол': 'table',
#     'стул': 'chair',
# }
#
#
# # функция для распечатки словаря
# def print_voc():
#     print('Сейчас словарь содержит: ')
#     for k, v in voc.items():
#         print(k, '—', v)
#
#
# # загружаем словарь из файлов
# try:
#     with open('dict.dat', 'rb') as dump_in:
#         voc = pickle.load(dump_in)
#
# except FileNotFoundError:
#     with open('dict.dat', 'wb') as dump_out:
#         pickle.dump(voc,dump_out)
#     print('Создан минимальный словарь')
#     print_voc()
# while True:
#     temp = input('\nВведите слова для перевода или # для завершения: ')
#     word = temp.strip().lower()
#     if word == '#' or word == '№':
#         break
#     if word in voc.keys():
#         translate = voc[word]
#         print(f'Cлово "{word}" переводится как {translate}.\n')
#     else:
#         print(f'Значение слова {word} отсутствует в словаре')
#         new_key = f'А как слово {word} переводится.\n '
#         new_key += 'Если ничего не вводите нажмите ENTER,\n '
#         new_key += 'Или введите его здесь: '
#         new_word = input(new_key)
#
#         if new_word != '' or len(new_word) > 2 :
#             voc[word] = new_word
#             print(f'Слово "{word}" с переводом "{new_word}" внесено в словарь.')
#         else:
#             print('Ничего не введено или слишком короткое слово.')
#             continue
# print('До новых встреч!')
# # Сохранить словарь
# with open('dict.dat', 'wb') as dump_out:
#     pickle.dump(voc,dump_out)


# Задача 2.
# while True:
#     a = input('Введите первое число: ')
#     b = input('Введите второе число: ')
#
#     if a.isdigit() and b.isdigit():
#         if int(b) == 0:
#             print('На ноль делить нельзя')
#         else:
#             print(int(a) / int(b))
#             break
#     else:
#         print('Вводить надо только числа')


# while True:
#     try:
#         a = input('Введите первое число: ')
#         b = input('Введите второе число: ')
#         c = int(a) / int(b)
#     except ValueError:
#         print('Только целые числа.')
#     except ZeroDivisionError:
#         print('На ноль делить нельзя.')
#     else:
#         print(f'{a}/{b} = {int(c)}')
#         break


# Задача 1.

# Мое решение.
# lst = [1,2,3,4,5,6,7,8,9]
# loop = True
# while loop:
#     try:
#         index = int(input('Введите индекс: '))
#         print(f'Число по индексу {index}: {lst[index]}')
#     except IndexError:
#         print('Вы вышли за диапазон.')
#     except ValueError:
#         print('Требуется ввести целое число.')
#     else:
#         loop = False

# Решение преподавателя
# lst = [1,2,3,4,5,6,7,8,9]
# try:
#     index = int(input('Введите индекс:'))
#     if not -len(lst) < index < len(lst) - 1:
#         raise ValueError('Индекс вне диапазона.')
#     res = lst[index]
#     print(f'Число по индексу {index}: {lst[index]}')
# except ValueError as exp:
#     mess = exp.args
#     if mess[0].startswith('invalid literal'):
#         print(f'Вводить надо числа')
#     else:
#         print(exp)


# Утверждения (assertion)
# В основном - для нужд тестирования
# try:
#     text = input('Введите текст: ')
#     assert len(text) > 3 # это утверждение, если False -> получаем AssertionError
# except AssertionError:
#     print('Слишком коротки текст.')

# "Бросаемся" исключениями - raise
# max_val = 10
# min_val = 1
#
# try:
#     val = int(input(f'Введите число в диапазоне от {min_val} до {max_val}: '))
#     if not min_val < val < max_val:
#         raise ValueError('Введенное число вне диапазона.')
#     print(f'Введенное число {val} лежит в заданном диапазоне.')
#
# except ValueError as exp:
#     print('Надо быть внимательнее:',exp)

# print('Остаток от деления:')
# loop = True
# while loop:
#
#     try:
#         value = int(input('На что делим число 10:'))
#         res = 10 % value
#         print(f'Остаток от деления 10 на {value} = {res}')
#     except ZeroDivisionError:
#         print('На ноль делить нельзя!')
#     except ValueError:
#         print('Надо вводить только целые числа.')
#     except Exception as exp: # Любое исключение в переменной exp
#         print('Произошло исключение:', exp.__class__.__name__,'|',exp)
#     else:
#         loop = False

###########################################
# flag = False # открывался ли на запись
#
# try:
#     fo = open('information.txt', encoding='utf-8')
# except FileNotFoundError:
#     fo = open('information.txt', 'wt', encoding='utf-8')
#     flag = True
#     print('Файл не обнаружен и создан с параметрами по умолчанию.')
#     # with open('information.txt', 'wt', encoding='utf-8') as fo:
#     #     fo.write('По умолчанию.')
# else:
#     print('Файл открыт успешно. Читаем его.')
#     print(fo.read())
#     fo.close()
# finally:
#     if flag:   # если файл был открыт на запись (было исключение)
#         fo.write('По умолчанию.')
#         fo.close()
#     print('Продолжаем работать.')
############################################

# res = []
# with open('info.txt', 'rt') as f:
#    while temp := f.readline().rstrip('\n'):
#        res += temp.split(', ')
#
# # res = set(list(map(lambda x: x.rstrip('\n'),res)))
# # res = set(res)
# res = sorted(int(x) for x in set(res))
#
# print(res)
# from path_lib import *
# print(img_dir)

# import pickle
# import pprint

# d = {
#     'стол': 'table',
#     'стул': 'chair',
# }

# # Сериализация
# with open('dictfile.dat', 'wb') as p:
#     # d - что сериализуем
#     # p - куда сериализуем
#     pickle.dump(d, p)

# # Десериализация
# with open('dictfile.dat', 'rb') as p:
#     d = pickle.load(p)
# pprint.pprint(d,width=15)
