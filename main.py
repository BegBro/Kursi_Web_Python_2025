# Исключения (runtime)
# try:
#   что пытаемся сделать
# except:
#   обрабатываем исключения
# else:
#   если исключения не было
# finally:
#   выполняется в любом случае
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



while True:
    try:
        a = input('Введите первое число: ')
        b = input('Введите второе число: ')
        c = int(a) / int(b)
    except ValueError:
        print('Только целые числа.')
    except ZeroDivisionError:
        print('На ноль делить нельзя.')
    else:
        print(f'{a}/{b} = {int(c)}')
        break


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
