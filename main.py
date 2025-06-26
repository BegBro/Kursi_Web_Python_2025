# match - case (3.10 >)
flag = True
print('Возможные ходы:\n\tL - влево\n\tR - вправо\n\tF - прямо, Q - выход')

while flag:
    ch = input('Ваш выбор: ')
    match ch:
        case 'L' | 'l' | 'Д' | 'д':
            print('Свернули налево.')
        case 'R' | 'r' | 'К' | 'к':
            print('Свернули направо.')
        case 'F' | 'f' | 'А' | 'а':
            print('Пошли прямо.')
        case 'Q' | 'q' | 'Й' | 'й':
            print('До свидания!')
            flag = False
        case _:
            print('Выбор неясен.')
