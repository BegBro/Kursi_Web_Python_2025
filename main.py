# Cписки (list)
# Имитация стека

N = 5

lst = []  # пустой список

for i in range(N):
    print(f'Кладём книгу {i + 1} в стопку.')
    lst.append(i + 1)

print('')

while lst:
    item = lst.pop() # возвращаем счетчик в переменную item
    print(f'Берём книгу {item} из стопки.')



['append', 'clear', 'copy', 'count', 'extend',
 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']