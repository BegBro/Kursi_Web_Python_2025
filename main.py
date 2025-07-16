# Введение во Flask
# MVC - (Model View Controller)
from flask import Flask
from flask import url_for
app = Flask(__name__)
debug = False

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


@app.route('/image') # Для отображений картинок,музыки,видео CSS требуется поместить контент в специальную папку static
def show_image():
    return f'<img src="{url_for('static',filename='images/doberman2.jpg')}">'

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

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=debug)
