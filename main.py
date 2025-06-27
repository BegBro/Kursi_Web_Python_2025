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