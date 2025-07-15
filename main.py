# Базы данных (запись)


"""
1. Импорт библиотеки sqlite3
2. Подключаемся к БД
3. Назначить "курсор"
4. Работаем с БД (запросы и ответы)
5. Подтверждаем изменения (commit)
5. Отключаемся от БД
"""
import sqlite3  # пункт 1


class Crud:
    def __init__(self, db_path):
        self._conn = sqlite3.connect(db_path)
        self._cur = self._conn.cursor()

    def create(self, table_name, name, age):
        res = self._cur.execute(
            f"""
             INSERT INTO {table_name}(name,age)
             VALUES(?,?)
             """, (name, int(age))
        )
        self._conn.commit()

    def read(self, table_name):
        res = self._cur.execute(
            f'SELECT * FROM {table_name}'
        ).fetchall()
        for num, name, age in res:
            print(num, name, age)

    # method override (переопределяем метод уничтожения объекта)
    def __del__(self):
        self._cur.close()
        self._conn.close()

    def update(self, table_name, id_num, name=None, age=None):
        query = f'UPDATE {table_name} name = "{name}" , age = {age} WHERE id={id_num}'
        print(query)
        self._cur.execute(
            query
        )
        self._conn.commit()

    def delete(self, id_num, table_name):
        res = self._cur.execute(
            f'DELETE {table_name} WHERE id={id_num}')
        self._conn.commit()


db = Crud('db/movies.sqlite')
# db.delete(9,'users')
# db.create('users', 'Дмитрий', 34)
db.update('users',11,'Евгений',18)
db.read('users')

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
