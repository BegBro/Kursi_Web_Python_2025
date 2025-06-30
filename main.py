# Кортеж (tuple, immutable)
N = 3
stud_lst = []

for _ in range(N):
    stud, aver = input('Введите фамилию студента:'), float(input('Введите средний балл студента:'))
    stud_lst.append((stud, aver))

for st in stud_lst:
    stud,aver = st
    print(f'Студент: {stud} Средний балл: {aver}',end='\n')
