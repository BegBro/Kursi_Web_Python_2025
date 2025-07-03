# Анонимные функции (однострочные, безымянные)
# lambda-функции
# lambda <аргументы>:<выражения>
# словарные выражения
# ключ сортировки



# fruits = ['ананас', 'банан', 'ежевика', 'арбуз', 'малина']
# # print(fruits.sort())  # Аргумент sort() сортирует список на месте и не возвращает ничего
#
#
# print(sorted(fruits, key= lambda s: (len(s),s[-1]))) # сначала сортирует по первой букве, потом по последней
#
#
# goods = [
#     ['Утюг', 1000,2],
#     ['Фен', 1000,5],
#     ['Телевизор', 8000,3]
# ]
#
# print(sorted(goods,key=lambda s:(s[1],s[2],s[0])))



# numbers = [1, 2, 3, 4, 5]
# squares = {n: n**2 for n in numbers}
# print(squares)
#
#
# squares = {n: n**2 for n in range(1,11) if n % 2 == 0}
# print(squares)
#
# sours_dict = {
#     'x': 1,
#     'y': 2,
#     'z': 3,
# }
#
# dest_dict = {k: v * 2 for k,v in sours_dict.items()}
# print(dest_dict)


# ENGLISH_ABC = [chr(ch) for ch in range(ord('a'), ord('z') + 1)]
# RUSSIAN_ABC = [chr(ch) for ch in range(ord('а'), ord('я') + 1)] + ['ё']
# ABC = set(ENGLISH_ABC) ^ set(RUSSIAN_ABC) ^ set(ENGLISH_ABC) ^ set(map(str.upper, ENGLISH_ABC)) ^ set(
#     x.upper() for x in RUSSIAN_ABC)
# # print(ABC)
#
# # print(ENGLISH_ABC)
# # print(RUSSIAN_ABC)
#
# # txt = 'Взрывной волной повредило остекление в заселённой части здания. Жителей дома эвакуировали. Другой БПЛА упал на парковку одного из предприятий Ельца, после чего возник пожар. Сотрудники ближайших цехов были эвакуированы. '
# txt = ('Я знаю, что я ничего не знаю.'
#        ' Но другие не знают и этого. А значит, я знаю больше, чем они')
#
# d = {}
#
#
# def remove_punctuation(text):
#     return ''.join(filter(lambda x: x in ABC ^ {' '}, text.lower()))
#
#
# def get_words(text: str) -> list:
#     return remove_punctuation(text).split()
#
#
# def longs_words(text, length=4) -> filter:
#     return filter(lambda word: len(word) >= length, get_words(text))
#
#
# words = get_words(txt)
#
# # Считаем частоту слов
# for word in words:
#     if word in d:
#         d[word] += 1
#     else:
#         d[word] = 1
#
# res = {k: v for k, v in sorted(d.items(), key= lambda item: item[1], reverse=False) }
#
# for k,v in res.items():
#     print(k,v)
#
#
# fruits = ['ананас','банан','ежевика','малина','арбуз']
#
# print(sorted(fruits, key=lambda ch:len(ch)))


# text = ''.join(filter(lambda x: x in ABC ^ {' '},text.lower()))
# print(text)

# print(remove_punctuation(txt))
# print(list(longs_words(txt, )))

# в одну строку вывести список квадратов чисел от 3 до 15
# [9,16,25...]
#
# res = list(map(lambda x: x ** 2, range(3, 16)))
# res_2 = [y ** 2 for y in range(3, 16)]
# print(res)
# print(res_2)
#
# words = ['В', 'этом', 'списке', 'останутся', 'слова',
#          'длина', 'которых', 'больше', 'шести']
#
# long_words = [word for word in words if len(word) > 6]
# print(long_words)
