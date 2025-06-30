# ДЗ

# stop_list =[] # список запрещенных слов

# Текст на входе, список на выходе, пронумерованный и отсортированный. Вывести разрешенные слова в список.

"""
stop_list = ['я', 'море', 'чистое']
text = 'Я люблю море Я лечу на море Я умею плавать в море Какое чистое море Хочу на море Завтра поедем на море Корабль плавает по морю'

res = set(text.lower().split())
res = list(res)
for word in res:
    if word in stop_list:
        res.remove(word)

res.sort()

for i,v in enumerate(res):
    print(f'{i+1}.{v}')
"""

stop_list = {'я', 'море', 'чистое'}
text = 'Я люблю море Я лечу на море Я умею плавать в море Какое чистое море Хочу на море Завтра поедем на море Корабль плавает по морю'

res = set(text.lower().split())

res = res - stop_list
res = sorted(res)

for i,v in enumerate(res):
    print(f'{i+1}.{v}')
