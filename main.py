"""
# Строки (immutable)
#    012345 - индекс str
s = 'Python'
# s[3] = 'y' error (immutable)
print(s[0])
print(s[3])
print(f'Длина слова: {len(s)}')
print(s[-1]) # индекс может быть отрицательным (будет считать с конца)
"""

v = 0
s = 'язык python'
for ch in s:
    # if ch in {'a','я','у','ю', 'о', 'ё', 'э', 'ы', 'и','y','o'}:
    #     v += 1
    if ch in 'аяуюоёэыиуоyo':
        v += 1
print(f'Число гласных в слове "{s}" = {v}.')


# Перебор строки по числовому индексу

for index in range(len(s)):
    print(s[index])
