# Декораторы
def answer(question):
    return 'думайте сами'


def dialog():
    def answer(question):
        if question.lower().startswith('когда'):
            return 'Никогда'
        else:
            return 'Упсссс'

    question = input()
    while question != '':
        print(answer(question))
        question = input()


dialog()



# Погода через API

# import requests
# from PIL import Image
# import io
#
# API_KEY = '694f7ce0804219a03398c767eb103225'
# URL = 'http://api.openweathermap.org/data/2.5/weather'
# CITY = 'Москва'
#
# params ={ # Из документации OPENWEAHER
#     'q': CITY, # Город
#     'appid': API_KEY, # Api_key
#     'units': 'metric', # система измерений
#     'lang': 'ru' # язык
# }
#
# response = requests.get(URL, params=params,)
# result = response.json()
#
# weather = result['weather'][0]['description']
# temperature = result['main']['temp']
# humidity = result['main']['humidity']
# wind = result['wind']['speed']
# data = result['coord']
# ll = f'{data['lon']},{data['lat']}'
# # print(ll)
#
# print(f'Сегодня в городе {CITY} : {weather} ')
# print(f'Температура : {temperature:.1f}°C')
# print(f'Влажность: {humidity}%')
# print(f'Скорость ветра: {wind} м/с')
#
# link = f'https://static-maps.yandex.ru/1.x/?ll={ll}&spn=0.005,0.005&l=sat&pt={ll},pm2dgl'
# image = requests.get(link).content
# if image:
#     im = Image.open(io.BytesIO(image)).convert('RGB')
#     im.save('map.png')


# Базы данных (запись)


# """
# 1. Импорт библиотеки sqlite3
# 2. Подключаемся к БД
# 3. Назначить "курсор"
# 4. Работаем с БД (запросы и ответы)
# 5. Подтверждаем изменения (commit)
# 5. Отключаемся от БД
# """
# import sqlite3  # пункт 1
#
#
# class Crud:
#     def __init__(self, db_path):
#         self._conn = sqlite3.connect(db_path)
#         self._cur = self._conn.cursor()
#
#     def create(self, table_name, name, age):
#         res = self._cur.execute(
#             f"""
#              INSERT INTO {table_name}(name,age)
#              VALUES(?,?)
#              """, (name, int(age))
#         )
#         self._conn.commit()
#
#     def read(self, table_name):
#         res = self._cur.execute(
#             f'SELECT * FROM {table_name}'
#         ).fetchall()
#         for num, name, age in res:
#             print(num, name, age)
#
#     # method override (переопределяем метод уничтожения объекта)
#     def __del__(self):
#         self._cur.close()
#         self._conn.close()
#
#     def update(self, table_name, id_num, name=None, age=None):
#         query = f'UPDATE {table_name} name = "{name}" , age = {age} WHERE id={id_num}'
#         print(query)
#         self._cur.execute(
#             query
#         )
#         self._conn.commit()
#
#     def delete(self, id_num, table_name):
#         res = self._cur.execute(
#             f'DELETE {table_name} WHERE id={id_num}')
#         self._conn.commit()
#
#
# db = Crud('db/movies.sqlite')
# # db.delete(9,'users')
# # db.create('users', 'Дмитрий', 34)
# db.update('users',11,'Евгений',18)
# db.read('users')

# import csv


# Подключаемся

# connection = sqlite3.connect('db/movies.sqlite')

# Назначаем курсор

# cursor = connection.cursor()

# Запрос (с помощью курсора)
# with open('people.csv','r',encoding='utf-8') as f:
#     reader = csv.reader(f,delimiter=',')
#     next(reader) # пропустить заголовок (первая строка)
#     for name,age in reader:
#         cursor.execute(
#             """
#             INSERT INTO users(name,age)
#             VALUES(?,?)
#             """,(name,int(age))
#     )

# connection.commit() # Подтверждение
# connection.close() # Закрываем подключение

# fetchall - всё
# fetchone - первое соответствие
# fetchmany(i) - i соответствий
# array = result.fetchall()

# print(array)

# for title, year in array:
#     print(title, year)
