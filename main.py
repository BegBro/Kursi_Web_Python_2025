# Подбор по росту
# 150 < height < 180
# Число кандидатов
# Число, кто прошел по критерию
# Среди прошедших min и max
total = 0
total_success = 0
min_val = float('inf')
max_val = float('-inf')

while (height := int(input('Введите рост кандидата: '))) != -1:
    if 150 <= height <=180:
        total_success +=1
        if height < min_val:
            min_val = height
        if height > max_val:
            max_val = height
    total += 1
print(f'Минимальный рост кандидата: {min_val}')
print(f'Максимальный рост кандидата: {max_val}')
print(f'Кол-во прошедших кандидатов: {total_success}')
print(f'Всего кандидатов: {total}')
