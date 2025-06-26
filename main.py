"""
# Циклы:
# while
while <условие(могут быть составные(or and и тд.))>:
    команды
# for
counter = 0  # обнуляем счётчик
# цикл из 5 итераций
while counter < 5:
    print(f'Итерация номер: {counter + 1}')
    # counter = counter + 1  # инкремент (увеличение на int (1))
    counter += 1  # инкремент (краткая запись) с помощью бинарного оператора
print(f'Итого в counter будет {counter}')
while counter > -1:
    print(f'До запуска: {counter}')
    counter-=1 # декремент (уменьшение на int(1))
print(f'Итого в counter будет {counter}')
"""

