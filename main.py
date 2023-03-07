from flask import Flask, url_for, request, render_template, redirect

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

user = "Ученик Лицея Академии Яндекса"


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')




@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/index')
    return render_template('login.html', title='Авторизация', form=form,
                           css_file=url_for('static', filename='css/styles.css'))


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
