alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
while True:
    print('Введите А чтобы зашифровать сообщение, Б чтобы расшифровать и В чтобы выйти')
    menu = input('>>> ').lower().strip()
    if menu == 'в':
        break
    elif not (menu == 'а' or menu == 'б'):
        continue
    output = ''
    message = input('Введите строку: ').lower().strip()
    key = int(input('Введите ключ: '))
    if menu == 'б':
        key *= -1
    for letter in message:
        if letter in alphabet:
            t = alphabet.find(letter)
            new_key = (t + key) % len(alphabet)
            output += alphabet[new_key]
        else:
            output += letter
    print('Результат: ' + output)
