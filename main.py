num = 3 # число, которое надо угадать
flag = True # флаг, изменяет значение по событию
var = ''

print('Я загадал число, угадай!')

while flag:
    var= int(input('Ваше значение: '))
    if var == num:
        print('Ура. Угадал!')
        flag = not flag # flag инвертирован (flag = False)
    elif var > num:
        print('Ваше число больше загаданного.')
    else:
        print('Ваше число меньше загаданного.')
print('Приходи еще!')
