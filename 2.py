from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
# @app.route('/index')
def index():
    return "Миссия Колонизация Марса"


@app.route('/promotion')
def promotion():
    return '<br>'.join(['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
                        'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!'])


@app.route('/index')
def second_page():
    return '''И на Марсе будут яблони цвести!'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
