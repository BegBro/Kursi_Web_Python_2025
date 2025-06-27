"""
word = input('Введите фразу для зашифровки:')
for i in range(len(word)):
    print(ord(word[i]))
"""
# Зашифровываем
s = set()
# word = input('Введите фразу для зашифровки:')
word = 'Пиво'
for ch in word:
    s.add(ord(ch))
print(s)

# Расшифровываем
res = ''
for i in s:
    res += chr(i)
print(res)
