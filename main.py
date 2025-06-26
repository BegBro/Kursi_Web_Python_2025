
# while (height := int(input('Введите свой рост: '))) < 150 or height > 180:
#     print('Вы не подходите.Позовите следующего.')
# print('Вы подходите.Проходите.')

height = int(input('Введите рост: '))

while not (150 <= height <= 180):
    print(f'Рост кандидата {height} не подходит')
    height = int(input('Введите рост: '))

print('Кандидат выбран.')
