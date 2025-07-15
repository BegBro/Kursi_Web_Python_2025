# Базы данных (запись)



"""
1. Импорт библиотеки sqlite3
2. Подключаемся к БД
3. Назначить "курсор"
4. Работаем с БД (запросы и ответы)
5. Подтверждаем (commit)
5. Отключаемся от БД
"""
import sqlite3  # пункт 1
# Подключаемся

connection = sqlite3.connect('db/movies.sqlite')

# Назначаем курсор

cursor = connection.cursor()

# Запрос (с помощью курсора)
result = cursor.execute(
    """
    INSERT INTO
    users(name,age)
    VALUES('Paul',28)
    """
)

connection.commit() # Подтверждение
connection.close() # Закрываем подключение

# fetchall - всё
# fetchone - первое соответствие
# fetchmany(i) - i соответствий
# array = result.fetchall()

# print(array)

# for title, year in array:
#     print(title, year)

