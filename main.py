# Коллекции - (set, list, dict, tuple)
# Множество - набор данных любого типа
s = set()  # пустое множество
# print(dir(s)) - список методов множества
s = {3, '5', '7', '3', '3'}
# добавление
s.add('8.5')
s.add(True)
# удаление
s.remove('3') # удаляет объект из множества, но вызывает ошибку если такого нет
s.discard('3') # удаляет вслепую
# s.clear() - очищает множество
temp = s.pop() # удаляет случайный и возвращает его
print(temp)
print(type(s))  # класс
print(f'Число элементов в s = {len(s)}')
print('Присутствует ли 3')
if str(3) in s:
    print('Да')
else:
    print('Нет')
for item in s:
    if item == '3':
        print(item)

# 'add', 'clear', 'copy', 'difference', 'difference_update',
# 'discard', 'intersection', 'intersection_update', 'isdisjoint',
# 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference',
# 'symmetric_difference_update', 'union', 'update'
