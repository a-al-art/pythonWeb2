from flask import Flask, url_for, request, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from werkzeug.security import generate_password_hash, check_password_hash
from data.news import News
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

user = "Ученик Лицея Академии Яндекса"

DEBUG_MODE = True


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


def main():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    user = db_sess.query(User).first()
    if user is None:
        tmp_fill_base()
        user = db_sess.query(User).first()
    if DEBUG_MODE:
        print(user.name)
        for user in db_sess.query(User).all():
            print(user)




    app.run()  # app.run(port=8080, host='127.0.0.1')


def tmp_fill_base():
    user = User()
    user.name = "Админ"
    user.about = "биография пользователя 1"
    user.email = "admin@email.com"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    news = News(title="Первая новость", content="Привет блог!",
                user_id=1, is_private=False)
    db_sess.add(news)
    db_sess.commit()


if __name__ == '__main__':
    x = generate_password_hash('123')
    print(x)
    print(check_password_hash(x, '123'))
    main()
