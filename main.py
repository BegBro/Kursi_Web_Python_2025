# Функции (Do not Repeat Yourself:DRY)
# Scope(local or global)
# Синтаксис:
# def <имя функции>([параметры])
#   команды

person = 'Пётр' # global scope глобальная переменная
count = 0
def greet_to_name(name='NoName'):
    print('Привет',name)
    print(count)


def increment():
    global count
    count +=1


def print_list(array):
    if array is None:
        array = []
    for item in array:
        print(item)


# def increment(count): # Приходит копия глобальной переменной count
#     count +=1


increment()
greet_to_name(person)
greet_to_name()
print_list(['Мяу', 'Гав'])

