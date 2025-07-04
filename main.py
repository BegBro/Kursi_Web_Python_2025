# Встроенные библиотеки
# PyPI - Python Package Index (pypi.org) # Сайт библиотек для Python
# import math as m
# Рекомендуется так не делать:
# from math import * # Загружается все пространство имен в память
from math import pi,sqrt,sin,radians

print('Число Пи:', pi)
print('Квадратный корень 4:', int(sqrt(4)))

# print(dir(m))
# print(help(m.cos))
print('Синус 30°:', round(sin(radians(30)), 2))


# # Функция sum - суммирует итерируемый объект
# lst = [1,2,3,100,23,-56]
# # res = 0
# # for x in lst:
# #     res += x
# res = sum(lst)
# min_value = min(lst)
# max_value = max(lst)
# print(res,min_value,max_value)
