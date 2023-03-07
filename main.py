from flask import Flask, url_for, request, render_template

app = Flask(__name__)

user = "Ученик Лицея Академии Яндекса"
@app.route('/')
@app.route('/index')
def main_page():
    return render_template('index.html', title='Домашняя страница', username=user,
                           css_file=url_for('static', filename='css/styles.css'))


@app.route('/second_page')
def second_page():
    return render_template('second.html', title='Вторая страница', username=user,
                           css_file=url_for('static', filename='css/styles.css'))



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')