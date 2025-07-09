class Sorter:
    def __init__(self):
        self.words = []

    def add_word(self,word):
        self.words.append(word)

    def result(self):
        return sorted(self.words, key= lambda x: len(x), reverse=True)


class Separator:
    def __init__(self):
        self.odd = []  # нечётные
        self.even = []  # чётные

    def add_num(self, num):
        if num % 2 == 0:
            self.even.append(num)
        else:
            self.odd.append(num)

    def get_odd(self):
        return self.odd

    def get_even(self):
        return self.even


class Clicker:
    def __init__(self):
        self._counter = 0

    def click(self):
        self._counter += 1

    def get_counter(self):
        return self._counter

    def reset(self):
        self._counter = 0


class Car:
    counter = 0  # Статичное свойство ("счетчик машин")

    def __init__(self, brand='NoBrand', model='NoModel', color='NoColor'):
        self.brand = brand  # 'BMW'  # Экземплярные поля, они создаются с каждым новым экземпляром класса
        self.model = model  # 'M3'   # Экземплярные поля, они создаются с каждым новым экземпляром класса
        self.color = color  # 'black'# Экземплярные поля, они создаются с каждым новым экземпляром класса
        self.engine_on = False  # Экземплярные поля, они создаются с каждым новым экземпляром класса
        Car.counter += 1

    def set_brand(self, new_brand):
        if new_brand:
            self.brand = new_brand

    def set_model(self, new_model):
        if new_model:
            self.model = new_model

    def set_color(self, new_color):
        if new_color:
            self.color = new_color

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_color(self):
        return self.color

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
