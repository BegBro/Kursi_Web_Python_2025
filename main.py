# Кортеж (tuple, immutable)
# Методы строки split() и join()

text = '192 и также 168 и также 0 и также 1'
ip = '192.168.0.1'

lst = text.split(' и также ')

print(lst)
text2 = ' и также '.join(lst)

print(text2)