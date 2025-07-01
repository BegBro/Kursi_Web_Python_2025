# ДЗ: Функция, которая выводит число словами 56 -> пятьдесят шесть
def num_to_word(num):
    # e = num % 10
    # g = int(num / 10)

    le = {0: 'ноль',
          1: 'один',
          2: 'два',
          3: 'три',
          4: 'четыре',
          5: 'пять',
          6: 'шесть',
          7: 'семь',
          8: 'восемь',
          9: 'девять',
          }
    lst = []
    while num != 0:
        temp = num % 10
        num = int(num / 10)
        if temp in le.keys():
            lst.append(le[temp])
    lst.reverse()

    return print(lst)

    # if e in le.keys():
    #     e = le[e]
    # if g in le.keys():
    #     g = le[g]
    # lst = [g,e]
    # return lst


num_to_word(55889644)
