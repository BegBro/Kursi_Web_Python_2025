class Car:
    counter = 0 # Статичное свойство ("счетчик машин")

    def __init__(self, brand='NoBrand', model='NoModel', color='NoColor'):
        self.brand = brand  # 'BMW'  # Экземплярные поля, они создаются с каждым новым экземпляром класса
        self.model = model  # 'M3'   # Экземплярные поля, они создаются с каждым новым экземпляром класса
        self.color = color  # 'black'# Экземплярные поля, они создаются с каждым новым экземпляром класса
        self.engine_on = False       # Экземплярные поля, они создаются с каждым новым экземпляром класса
        Car.counter += 1

    def start_engine(self):
        self.engine_on = True

    def drive_to(self, place):
        if self.engine_on:
            print(f'Едем в {place}. На {self.brand} {self.model}.')
        else:
            print('Двигатель не заведён, не едем.')

    @staticmethod
    def get_counter():
        return Car.counter


class Person:
    def __init__(self, name='Bill', age=1):
        # свойства (поля) класса
        self._name = name
        self._age = age

    def set_name(self, new_name):
        if new_name:
            self._name = new_name

    # setters
    def set_age(self, new_age):
        if 0 < new_age < 150:
            self._age = new_age
        else:
            print('Некорректный возраст - ', new_age)

    # getter
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def person_info(self):
        print(f'Человек с именем {self._name}. Возраст {self._age}.')


def summ(a, b):
    return a + b


def diff(a, b):
    return a - b


if __name__ == '__main__':
    print('Это библиотека, а исполняемый - main.py')
