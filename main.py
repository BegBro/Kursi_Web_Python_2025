"""
word = '        статор              '

print(word.strip())
print(word.lstrip())
print(word.rstrip())
"""

temp =int(input('Введите слово: ').strip())
word = 'ротор'

print(word.strip('р')) # Убирает символ 'р' c краёв str
