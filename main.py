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

a = ['a','b','c']
b = a[:] # a.copy()
b.append('d') # b += ['d']
print(id(a))
print(id(b))

print(a)
print(b)
"""['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']"""