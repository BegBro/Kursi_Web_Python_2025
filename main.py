import sys
print('Я', sys.argv[0], 'и мой аргумент', sys.argv[1])

if len(sys.argv) >= 2:
    match sys.argv[1]:
        case 'p':
            print('Привет.')
        case 'g':
            print('Пока')
        case _:
            print('Не понял')
