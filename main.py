# Кортеж (tuple, immutable)
# Функция enumerate() - в цикле for возвращает пару (i, v) (Нумерует)

fio = {'Петров','Иванов','Бурунов'}

for i,v in enumerate(fio):
    print(f'{i+1}.{v}')
