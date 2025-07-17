# Введение во Flask
# MVC - (Model View Controller)
# GET - запрашивает данные (read)
# POST - отправляет данные на сервер (submit)
# PUT - принудительно заменяет всё на сервере из контекста запроса ("замена")
# DELETE - удаляет указанные данные ("удалить")
# PATCH - частичное изменение данных
import os.path

from flask import Flask, url_for, request
from werkzeug.utils import secure_filename
import sqlite3

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
ALLOWED_EXTENSIONS = ['txt', 'pdf', 'zip', 'jpg', 'png']
debug = False
y = 5


def allowed_file(filename):
    return ('.' in filename and
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS)


@app.route('/')
@app.route('/index')
def index():
    print('Вызвана функция index')
    return 'Привет, Flask'


@app.route('/about')
def about():
    print('Вызвана функция about')
    return 'О нас'


@app.route('/countdown')
def cd():
    lst = [str(x) for x in reversed(range(10))]
    lst.append('Полетели!!!')
    return '<br>'.join(lst)


@app.route('/image')  # Для отображений картинок,музыки,видео CSS требуется поместить контент в специальную папку static
def show_image():
    return f'<img src="{url_for('static', filename='images/doberman2.jpg')}">'


@app.route('/sample_page')
def sample_page():
    return f"""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Картинка Добермана</title>
</head>
<body>
  <img src="{url_for('static', filename='images/doberman2.jpg')}" alt="Dober">
</body>
</html>
    """


@app.route('/sample_page2')
def sample_page2():
    with open('temp.html', 'r', encoding='utf-8') as html:
        return html.read()


# @app.route('/1')  ТАК ДЕЛАТЬ НЕ НАДО
# def show_num():
#     global y
#     y += 1
#     return str(y)


# <string> - по умолчанию строка
# <int:number> - целое число
# <float:number> - дес. дробь
# <path:p> - может содержать слеши для указания пути
# <uuid:id> - строка-идентификатор (16-байт в HEX-формате)
@app.route('/greeting/<user>/<int:id_num>')
def greeting(user, id_num):
    return f'Привет, {user} c id={id_num}'


@app.route('/get_user/')
@app.route('/get_user/<int:id_num>')
def get_user(id_num=None):
    if id_num is None:
        return 'Нет номера записи.'
    con = sqlite3.connect('db/movies.sqlite')
    cur = con.cursor()
    data = cur.execute(
        f"""
        SELECT name,city
        FROM users
        WHERE trip_id={id_num}
        """
    ).fetchone()
    # print(data) # Для отладки
    name, city = data
    cur.close()
    cur.close()
    return f'''<table border=1>
    <tr>
    <td>ФИО</td>
    <td>Город</td>
    </tr>
    <tr>
    <td>{name}</td>
    <td>{city}</td>
    </tr>
    </table>'''


@app.route('/form_test', methods=['POST', 'GET'])
def form_test():
    if request.method == 'GET':
        with open('form.html', 'r', encoding='utf-8') as html:
            return html.read()
    elif request.method == 'POST':
        print(request.form['gender'])
        print(request.form['email'])
        print(request.form['about'])
        return 'Форма успешно отправлена'


@app.route('/upload', methods=['POST','GET'])
def file_upload():
    if request.method == 'GET':
        with open('upload.html', 'r', encoding='utf-8') as html:
            return html.read()
    elif request.method == 'POST':
        # print(request.files)
        if 'file' not in request.files:
            return 'Файл не был выбран'

        file = request.files['file']

        if file.filename == '':
            return 'Файл не был выбран'

        if file and allowed_file(file.filename):
            new_name = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_name))
            return f'Файл {new_name} загружен успешно'

    return 'Ошибка загрузки'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=debug)
