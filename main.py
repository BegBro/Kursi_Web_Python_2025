"""
# Списочные выражения (list comprehension)
# squares = []
# for i in range(10):
#     squares.append(i ** 2)
# Список квадратов чисел
squares = [i**2 for i in range(10)] # на первом месте что попадёт в список, на втором закономерность

# список квадратов чётных чисел
squares = [i**2 for i in range(10) if i % 2 == 0] # на первом месте что попадёт в список, на втором закономерность, на третьем условие
#          что       закон            условие
print(*squares, sep=', ')

# произведение i и j
# print([i*j for i in range(3) for j in range(3)])

n = '100 200 300 400 500 600 700 800'
approved = [500,800]
a = [int(i) for i in n.split() if int(i) in approved]
print(a)
"""

text = 'Списочные выражения применяются для эффективности кода'
# text = text.split()
# res = [a for a in text if (text.index(a)+1) % 3 == 0]

res = [a for a in text.split() [2::3]]
print(res)
