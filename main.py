# Кортеж (tuple, immutable)

channels = ('red', 'green', 'blue')

r,g,b = channels # распаковка (кол-во переменных должно быть одинаково), работает с любой коллекцией
# r,*g = channels - r первый элемент, остальное g

print(r)
print(g)
print(b)

channels = [1, 2, 3]

r, *g = channels

print(g)

a,b = input(),input()
print(a,b)
