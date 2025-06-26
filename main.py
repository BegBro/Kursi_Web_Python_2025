# break, continue
num = 3 # число, которое надо угадать
flag = True # флаг, изменяет значение по событию
var = ''

print('Я загадал число, угадай!')

while True:
    var= int(input('Ваше значение: '))
    if var == num:
        print('Ура. Угадал!')
        break
    elif var > num:
        print('Ваше число больше загаданного.')
    else:
        print('Ваше число меньше загаданного.')
print('Приходи еще!')
