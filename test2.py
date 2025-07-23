from openpyxl.styles.builtins import title
from requests import get, post, put, delete

# print(get('http://localhost:5000/api/v2/news').json())
# print(get('http://localhost:5000/api/v2/news/1').json())
# print(post('http://localhost:5000/api/v2/news', json={}).json())

# print(post('http://localhost:5000/api/v2/news', json={'title' : 'aaaaaa'}).json())

print(post('http://localhost:5000/api/v2/news', json={'title': 'Заголовок через API2',
                                                      'content': 'Контент через API2',
                                                      'user_id': 2,
                                                      'is_private': 0}).json())
