# ДЗ: Функция, которая выводит число словами 56 -> пятьдесят шесть
def num_to_word(num):
    if str(num) > 2:
        return
    e = num % 10
    le = ['один','два']


# Функции (Do not Repeat Yourself:DRY)
# Return Value

def square(num):
    return num ** 2


def even_odd(num):
    if num % 2 == 0:
        return 'Чётное'
    return 'Нечётное'


def print_string(s=None):
    if s is None:
        return
    print(s)


t = square(5)
t = square(t)
print(even_odd(6))
print(t)
