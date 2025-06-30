# Кортеж (tuple, immutable)
# Функция sorted() # На вход итерируемый объект, на выходе сортированный список(list)
s = {'Петров','Иванов','Бурунов'}

lst = sorted(s,reverse=True)

# lst = list(s)
# lst.sort()

print(lst,sep=' ')
