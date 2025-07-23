from openpyxl.styles.builtins import title
from requests import get, post, put, delete

# print(get('http://localhost:5000/api/news').json())
# print(get('http://localhost:5000/api/news/1').json())
# print(get('http://localhost:5000/api/news/1000').json())
# print(get('http://localhost:5000/api/news/q').json())
# print(post('http://localhost:5000/api/news', json={}).json())
# print(post('http://localhost:5000/api/news', json={'title' : 'aaaaaa'}).json())
# print(post('http://localhost:5000/api/news', json={'title' : 'Заголовок',
#                                                    'content' : 'Контент',
#                                                    'user_id': 'Пять',
#                                                    'is_private':0}).json())
# print(delete('http://localhost:5000/api/news/500').json())
# print(delete('http://localhost:5000/api/news/5').json())

print(put('http://localhost:5000/api/news/1', json={}).json())
print(put('http://localhost:5000/api/news/1', json={'title': 'Заголовок'}).json())
