# Формат вывода 2
name = 'Игорь'
email = 'aaa@bbb.ru'
age = 32
weight = 98.655656

# 1 способ (плейсхолдеры)
# %s - string
# %d - digit (целое число)
# %f - float
print('Имя: %s, E-mail: %s, Возраст: %d' % (name, email, age))

# 2 способ
print('Имя: {}, E-mail: {}, Возраст: {}'.format(name, email, age))

# 3 способ (самый популярный с версии 3.6 - f-строка)
print(f'Имя: {name},E-mail: {email}, Возраст: {age}, Вес: {weight:.3f}')
