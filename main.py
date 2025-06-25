# Формат вывода
# \ = Управляющая последовательность. Начало escape sequence
# \n - перевод строки
# \t - табуляция
# \x - вызов символа 2-знакоместамписать в 16-чном формате (ASCII)
# \ - Экранирование символа (спрятать)
# \u - вызов символа 4-знакоместамписать в 16-чном формате(Unicode)
# Burned Again Shell = BUSH console = Linux console
# T ERMINAL
word1 = 'Пришел'
word2 = 'Увидел'
word3 = 'Победил'
word4 = '27\xB0С'
print(word1, word2, word3, sep=', ', end='->')
print(word4)
print("Концерт группы \"Кино\"")
print('Путь к файлу: С:\\Program Files\\bin')
