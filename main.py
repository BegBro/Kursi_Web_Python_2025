# Исключения (runtime)
# try:
#   что пытаемся сделать
# except:
#   обрабатываем исключения
# else:
#   если исключения не было
# finally:
#   выполняется в любом случае



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
