# Анонимные функции (однострочные, безымянные)
# lambda-функции
# lambda <аргументы>:<выражения>

ENGLISH_ABC = [chr(ch) for ch in range(ord('a'), ord('z') + 1)]
RUSSIAN_ABC = [chr(ch) for ch in range(ord('а'), ord('я') + 1)] + ['ё']
ABC = set(ENGLISH_ABC) ^ set(RUSSIAN_ABC) ^ set(ENGLISH_ABC) ^ set(map(str.upper, ENGLISH_ABC)) ^ set(x.upper() for x in RUSSIAN_ABC)
print(ABC)

# print(ENGLISH_ABC)
# print(RUSSIAN_ABC)
txt = 'Взрывной волной повредило остекление в заселённой части здания. Жителей дома эвакуировали. Другой БПЛА упал на парковку одного из предприятий Ельца, после чего возник пожар. Сотрудники ближайших цехов были эвакуированы. '
# text = ''.join(filter(lambda x: x in ABC ^ {' '},text.lower()))
# print(text)

def remove_punctuation(text):
    return ''.join(filter(lambda x: x in ABC ^ {' '},text.lower()))


def get_words(text: str) -> list:
    return remove_punctuation(text).split()


def longs_words(text,length=4) -> filter:
    return filter(lambda word: len(word) >= length,get_words(text))

print(remove_punctuation(txt))
print(longs_words(txt))

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
