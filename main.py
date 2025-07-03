# Анонимные функции (однострочные, безымянные)
# lambda-функции
# lambda <>,



# Функция, как объект
# Передаётся в другие функции: функции высшего порядка

# Функция критерия отбора элементов списка
# Критерий: длина слова
# def is_longer_six(word):
#     return len(word) > 6


# is_longer_six = lambda word: len(word) > 6


# Критерий - первая буква
# def is_first_letter_a(word):
#     return word[0] == 'а'

# is_first_letter_a = lambda word: word[0] == 'a'


# Критерий - вхождение подстроки
# В частности 'ан'
# def string_contains(s):
#     return 'ан' in s


# string_contains = lambda s: 'ан' in s
#
#
# def square(num):
#     return num ** 2
#
#
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9] # 123456789
# squares = map(square, nums)
# print(list(squares))
#
#
#
# words = ['В', 'этом', 'списке', 'останутся', 'слова',
#          'длина', 'которых', 'больше', 'шести']
#
# fruits = ['арбуз', 'ананас', 'банан', 'ежевика', 'малина']
#
# result = list(filter(lambda word: len(word) > 6, words))
# print(result)
#
# res = list(filter(lambda x: x[0] == 'а', fruits))
# print(res)
#
# for word in filter(lambda word: len(word) > 6, words):
#     print(word)
#
#
# res = list(filter(lambda s: 'ан' in s, fruits))
# print(res)
#

# def multy(first, *args):
#     # print(len(args)) # подсчёт числа аргументов
#     # print(args) # по индексу, либо перебором в цикле
#     # if len(args) == 0:
#     #     return 0
#     if not args:
#         return first
#     result = first
#     for arg in args:
#         result *= arg
#     return result
#
#
# def calc(*args: tuple, operator: str = '+') -> any:
#     match operator:
#         case '+':
#             result = 0
#             for i in args:
#                 result += i
#         case '*':
#             result = 1
#             for i in args:
#                 result *= i
#         case _:  # случай по default
#             return 'так нельзя'
#     return result
#
#
# def fio(name, surname):
#     return f'{name} {surname}'
#
#
# def sandwich(type_of_meal, with_onion=False, with_tomato=False):
#     print('Булочка')
#     if with_onion:
#         print('Лук')
#     print(type_of_meal)
#     if with_tomato:
#         print('Помидоры')
#     print('Булочка')
#
#
# def print_any(*args, **kwargs):
#     for i in args:
#         print(i)
#     for k, v in kwargs.items():
#         print(k, '=', v)
#
#
# def profile(name, surname, city, *children, **additional):
#     print('Имя:', name)
#     print(f'Фамилия: {surname}')
#     print(f'Из города: {city}')
#     if len(children) > 0:
#         print('Дети:', ', '.join(children))
#     if 'hobbie' in additional:
#         print('Хобби:', ', '.join(additional['hobbie']))
#     # print(additional)
#
#
# profile('Дмитрий', 'Колесов', 'Волгоград',
#         'Мария', 'Пётр', hobbie=['Филателия', 'Шахматы'])
# print_any('Дмитрий', 'Колесов', city='Москва', age=27)
# sandwich('котлета', with_onion=True)
# print(fio(surname='Бендер', name='Остап'))
# print(multy(2, 3, 4))
# print(calc(1, 2, 3, operator='*'))

# При распаковке '*' может быть только одна
# def coordinates() -> tuple:
#     return 5.4, 3.2, 3.8, 7.2, 4.6
#
#
# x, y, *rest = coordinates()  # распаковка
# print(f'x = {x}, y = {y}, rest = {rest}')
#
# *names, surname = 'Остап Сулейман Бендер'.split()
# print(names, surname)

# Применяем is на практике
# def print_array(array: list, start: int = None):
#     if start is not None and start > len(array):
#         return
#     if start is None:
#         start = 0
#     for i in range(start, len(array)):
#         print(array[i])
#
#
# a = [1, 2, 3]
# print_array(a)

# Оператор is: a is b -> когда a и b - один и тот же объект
# my_refregirator = ['колбаса', 'сыр', 'масло']
# # his_refregirator = ['колбаса', 'сыр', 'масло']
# his_refregirator = my_refregirator.copy()  # [:]
# # my_refregirator += ['мясо']
# print(his_refregirator)
# print(my_refregirator is his_refregirator)
# print(my_refregirator == his_refregirator)
# print(id(my_refregirator) == id(his_refregirator))
# temp = None
# print(type(temp))
# print(temp is None)
# Словарь также изменяем, как и множество со списком
# d = {'a': 1}
# print(id(d))
# d['a'] += 1
# print(id(d))

# def print_goodbye(arg):
#     print('Goodbye', end=' ')
#
# def print_cruel(arg):
#     print('cruel', end=' ')
#
# def print_world(arg):
#     print('world', end=' ')
#
# def main():
#     print_goodbye(1)
#     print_cruel(2)
#     print_world('3')
#
# main()

# def generate_list():
#     for i in range(5):
#         yield i  # генератор (возвращает, но не завершает)
#
#
# array = tuple(generate_list())
#
# print(array)
# PI = 3.1415
# # Shadows name 'square' from outer scope
# def greet(name):
#     print('Привет,', name)
#     name = 'друг'
#     print('Здравствуй,', name)
#
#
# def square_area(length: int, width: int) -> None:
#     area = length * width
#     print(f'Площадь площади = {area}')
#
#
# def circle_length(radius: float):
#     perimetr = 2 * PI * radius
#     print(f'Длина окружности с радиусом {radius} = {perimetr:.2f}')
#
#
# def print_array(array: list) -> None:
#     for item in array:
#         print(item)
#
#
# # Главная функция
# def main():
#     area = 'Дворцовая площадь'
#     words = ['Привет', 'мир']
#     greet('Пётр')
#     print('Давай встретимся, где', area)
#     square_area(320, 240)
#     print('Ну что? Встречаемся, где', area)
#     circle_length(5)
#     print_array(words)
#     print_array(['a', 'b', 'c'])
#
#
# main()

# Пример как делать не надо
# a = [1, 2]
#
# def change_array():
#     a[0] = 0
#
# change_array()
# print(a)

# # Функция с аннотацией
# num_to_str = {
#     0: 'ноль',
#     1: 'один',
#     2: 'два',
#     3: 'три',
#     4: 'четыре',
#     5: 'пять',
#     6: 'шесть',
#     7: 'семь',
#     8: 'восемь',
#     9: 'девять',
#     10: 'десять',
#     11: 'одиннадцать',
#     12: 'двенадцать',
#     13: 'тринадцать',
#     14: 'четырнадцать',
#     15: 'пятнадцать',
#     16: 'шестнадцать',
#     17: 'семнадцать',
#     18: 'восемнадцать',
#     19: 'девятнадцать',
#     20: 'двадцать',
#     30: 'тридцать',
#     40: 'сорок',
#     50: 'пятьдесят',
#     60: 'шестьдесят',
#     70: 'семьдесят',
#     80: 'восемьдесят',
#     90: 'девяносто'
# }
#
#
# def number_to_words(n: int) -> str:
#     """
#     Функция, принимающая число и возвращающее его словами
#     :param n: двузначное число
#     :return: это число словами
#     """
#     if len(str(n)) > 2:
#         return 'Введите двузначное число'
#     if len(str(n)) == 1 or n in num_to_str:
#         return num_to_str[int(n)]
#     return num_to_str[int(str(n)[0] + '0')] + ' ' + num_to_str[int(str(n)[1])]
#
#
# print(number_to_words(33))