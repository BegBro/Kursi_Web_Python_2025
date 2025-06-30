# Списки (List)
"""
s = {'3','4','5'}
lst = list(range(1,11))

print(lst)
"""
# lst=[] # пустой список
# lst = [1,2,23]
# lst = list('Python')
# lst = [1,2,3] * 3 # повторяется 3 раза

# a = ['a','b','c']
# b = a[:] # a.copy()
# b.append('d') # b += ['d']
# print(id(a))
# print(id(b))
#
# print(a)
# print(b)
"""['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']"""

"""
lst = []
while True:
    c = input('Введите а для того чтобы добавить ингредиент в список, введите пустую строку чтобы закончить список.:')
    if c == '':
        break
    else:
        lst.append(c)

lst.sort()

for i in range(len(lst)):
    print(str(i+1)+'.', lst[i])
"""

lst = []
while (item:= input('Ингредиент: ')) != '':
    lst.append(item)

temp = set(lst)
lst = list(temp)

print(f'У нас есть {len(lst)} ингредиентов.')
lst.sort()

for i in range(len(lst)):
    print(f'\t{i+1}.{lst[i]}')
