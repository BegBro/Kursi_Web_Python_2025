# Cписки (list)
# Создание аббревиатур

lst = []

while (word := input('Введите слово: ')).strip() != '':
    lst.append(word[0].upper())

print('Получилась аббревиатура:', *lst, sep='')
