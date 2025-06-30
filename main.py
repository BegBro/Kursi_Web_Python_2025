# Строки (immutable, iterable)
# Начало и окончание строки
# 1.find('подстрока')
# 2.find('подстрока', start)
# 3.find('подстрока', start)
"""
s= 'Cмотреть, вертеть, видеть'

index = s.find('р') # ищем с начала строки s
print(index)

index = s.find('р',10) # ищем с позиции __start в строке s
print(index)

index = s.find('ер',10,15) # ищем с позиции __start до __end
print(index)
"""

s = 'синхрофазотрон'
ch = 'о'

if ch in s:
    count = s.count(ch)
    print(f'Буква {ch} встречается {count} раз(а).')
    print('Её позиция/позиции:',end=' ')
    start = 0
    for i in range(count):
        pos = s.find(ch, start)
        start = pos + 1
        print(pos,end=' ')
else:
    print(f'Буквы {ch} нет в слове "{s}".')
