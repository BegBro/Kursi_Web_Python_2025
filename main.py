# Встроенные библиотеки
# PyPI - Python Package Index (pypi.org) # Сайт библиотек для Python



# import datetime as dt
# from time import strftime
#
# my_time = dt.time(15, 27, 32)
# print(my_time)
#
# my_date = dt.date(2025, 7, 15)
# print(my_date)
#
# my_date_time = dt.datetime.combine(my_date, my_time)
# print(my_date_time)
#
# date1 = dt.date(2025, 6, 15)
# date2 = dt.date(2025, 7, 3)
# delta = date2 - date1
#
# print(delta)


# print(dt.datetime.now())
# print(dt.datetime.now().date())
# print(dt.datetime.now().time())


# print(type(dt.datetime.now()))
#
# time = dt.datetime.now()
#
# ftime = time.strftime('%d.%m.%Y')
# print('Сегодня:',ftime)
#
# ftime = time.strftime('%H:%M')
# print('Время:', ftime)


# import random as r
# r.seed()
# print(r.random())

# abc = 'qwertyuiopasdfghjklzxcvbnm'
# num = '123456789'
# spec = '@#$&'
# N = 8
#
# abc = list(abc)
# num = list(num)
# spec = list(spec)
# r.shuffle(abc)
#
# temp = abc[:N - 3]
#
# temp.append(r.choice(abc).upper())
# temp.append(r.choice(num))
# temp.append(r.choice(spec))
# r.shuffle(temp)
#
# res = ''.join(temp)
#
# print(res)


# abc = 'qwertyuiopasdfghjklzxcvbnm'
# lst = list(abc) + ['1','2'] +['#','^','$']
# r.shuffle(lst)
# res = ''.join(lst[:8])
# print(res)

# lst = [1,2,3,4,5,6,7,8,9]
#
# for _ in range(10):
#     print(r.sample(lst,k = 5))


# zara = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685',]
# for _ in range(10):
#     print(r.choice(zara),r.choice(zara))


# d ={
#     'a' : 1,
#     'b' : 2,
#     'c' : 3,
# }
#
# keys = list(d.keys())
# key = r.choice(keys)
#
# print(d[key])

# lst = [1,2,3,4,5,6,7,8,9]
#
# print(r.choice(['орёл', 'решка']))
# print(r.choice('орёл'))

# for _ in range(10):
#     print(r.choice(lst))

# for _ in range(10):
#     # print(r.randint(0, 10))
#     print(r.randrange(0,10,2))

# import math as m
# Рекомендуется так не делать:
# from math import * # Загружается все пространство имен в память
# from math import pi, sqrt, sin, radians, hypot
#
# print('Число Пи:', pi)
# print('Квадратный корень 4:', int(sqrt(4)))
# print(dir(random))
# print(help(m.cos))


# print('Синус 30°:', round(sin(radians(30)), 2))
# print('Гипотенуза для 3 и 2 :', hypot(3,2))

# # Функция sum - суммирует итерируемый объект
# lst = [1,2,3,100,23,-56]
# # res = 0
# # for x in lst:
# #     res += x
# res = sum(lst)
# min_value = min(lst)
# max_value = max(lst)
# print(res,min_value,max_value)
