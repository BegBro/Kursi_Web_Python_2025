# Базовый синтаксис
```
SELECT перечень_полей (*)-все поля
FROM имя_таблицы - откуда выборка 
WHERE условие поиска - если не указанно, то подтягивается все 
```

# Выборка по году выпуска
```
SELECT * 
FROM films
WHERE year = 2010
```
# # Выборка по году выпуска и вывод только названий
```
SELECT title
FROM films
WHERE year = 2010
```
# Выбор названия и года в диапазоне отсортировано по годам выпуска
```
SELECT title,year     
FROM films
WHERE year > 2005 
AND year < 2010
AND duration < 90
ORDER BY year
```
# Тоже самое, но с BETWEEN (всегда включает границы)
```
SELECT title,year
FROM films
WHERE year BETWEEN 2005 AND 2010
ORDER BY year
```
# Пример не вполне корректного запроса
```
SELECT title
FROM films
WHERE genre = 8
```
# Исправим (составной вопрос)
```
SELECT title
FROM films
WHERE genre = (SELECT id 
FROM genres 
WHERE title = 'фантастика')
```
# 
```
SELECT title,duration
FROM films
WHERE duration IN (45,60,90)
ORDER BY duration DESC
```
# Группировка по id
```
SELECT *
FROM films
WHERE year >= 2001
AND duration BETWEEN 45 and 90
GROUP BY id
```
# Выборка с LIKE
```
SELECT title FROM films
WHERE title LIKE 'А_к%'
```
### Примечание:
- % - любое кол-во символов от 0 до INF
- _ - любой символ

# Выборка без повторов
```
SELECT DISTINCT year FROM films
ORDER BY year
```
### Примечание:
- DISTINCT
# 
```
SELECT 
films.title as Фильм,
genres.title as Жанр
FROM films,genres
WHERE films.genre = genres.id
```

# Выборка: сколько фильмов каких годов
```
SELECT 
films.title as Фильм,
genres.title as Жанр
FROM films,genres
WHERE films.genre = genres.id
```