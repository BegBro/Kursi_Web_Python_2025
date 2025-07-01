# ДЗ: Функция, которая выводит число словами 56 -> пятьдесят шесть
def num_to_word(num):
    if len(str(num)) > 2:
        return None

    e = num % 10
    g = int(num / 10)

    le = {1: 'один',
          2: 'два',
          3: 'три',
          4: 'четыре',
          5: 'пять',
          6: 'шесть',
          7: 'семь',
          8: 'восемь',
          9: 'девять',
          }

    if e in le.keys():
        e = le[e]
    if g in le.keys():
        g = le[g]
    lst = [g,e]
    return lst



f = num_to_word(14)
print(f)
