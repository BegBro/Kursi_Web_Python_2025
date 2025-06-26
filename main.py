# break, continue
counter = -1 # обнуляем счетчик
# цикл из 5 операции, но 3 пропускаем
while counter < 5:
    counter += 1
    if counter == 3:
        continue
    print(f'Итерация номер: {counter}')
