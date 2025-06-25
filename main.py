promt = """Витязь на распутье.
Налево(L) пойдешь, вольну-волю обретёшь...
Нараво(R) пойдешь, коня потеряешь...
Прямо(F) пойдешь, сыт и весел будешь..."""
print(promt)
choice = input('Куда идём (L,R или F) :')
if choice == 'L' or choice == 'l':
    print('Вольный горец.')
elif choice == 'R' or choice == 'r':
    print('Потерял коня.')
elif choice == 'F' or choice == 'f':
    print('Сыт и весел.')
else:
    print('Выбор не ясен.')
