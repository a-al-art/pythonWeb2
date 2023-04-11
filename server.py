import logging

from flask import Flask, url_for, render_template, redirect, session, make_response, jsonify, request
from flask_restful import Api
from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, PasswordField, BooleanField, SubmitField, FileField
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename
from flask_login import LoginManager, login_user

import news_resources
from alice_skill import handle_dialog
from data import db_session, news_api
from data.users import User
from data.news import News

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
api = Api(app)

login_manager = LoginManager()
login_manager.init_app(app)

DEBUG_MODE = True

# для алисы
SessionStorage = {}


@app.route('/post', methods=['POST'])
def alice_main():
    logging.info(f'Request: {request.json!r}')

    response = {
        'session': request.json['session'],
        'version': request.json['version'],
        'response': {
            'end_session': False
        }
    }
    handle_dialog(request.json, response, SessionStorage)
    logging.info(f'Response:  {response!r}')

    return jsonify(response)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class RegistrationForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    # TODO: повтор пароля и проверки
    name = StringField('Имя')
    # TODO: поле "о себе" -> about
    submit = SubmitField('Зарегистрироваться')


class AvatarForm(FlaskForm):
    file = FileField("Файл", validators=[DataRequired()])
    submit = SubmitField('Загрузить')


# TODO: logout

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found 404'}), 404)


@app.route('/avatar', methods=['GET', 'POST'])
def avatar():
    form = AvatarForm()
    if form.validate_on_submit():
        avatar_file = url_for('static', filename=f'img/loaded_{secure_filename(form.file.data.filename)}')
        avatar_file = avatar_file.lstrip('/')
        print(avatar_file)
        form.file.data.save(avatar_file)
        return render_template('avatar.html', form=form, avatar=avatar_file)
    return render_template('avatar.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            session['user_name'] = user.name
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user:
            return render_template('register.html',
                                   message="Пользователь с такой почтой уже зарегистрирован",
                                   form=form)
        add_user(form.email.data, form.password.data, form.name.data)
        # TODO: сообщение об успешной регистрации
        return redirect("/login")
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/')
@app.route('/index')
def main_page():
    session.permanent = True
    session['visits_count'] = session.get('visits_count', 0) + 1
    with open('visits.txt') as in_file:
        visits = int(in_file.read())
    visits += 1
    with open('visits.txt', 'w') as out_file:
        out_file.write(str(visits))
    return render_template('index.html', title='Домашняя страница',
                           username=session['user_name'] if 'user_name' in session else 'Гость',
                           visits=session['visits_count'], visits_server=visits,
                           css_file=url_for('static', filename='css/styles.css'))


@app.route('/second_page')
def second_page():
    return render_template('second.html', title='Вторая страница',
                           username=session['user_name'] if 'user_name' in session else 'Гость',
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

        print('---')
        for news in user.news:
            print(news)
        # Почему удалось создать новость от несуществующего пользователя?
        # news = News(title="Первая новость", content="Привет блог!",
        #             user_id=5, is_private=False)
        # db_sess.add(news)
        # db_sess.commit()
    app.register_blueprint(news_api.blueprint)
    # для списка объектов
    api.add_resource(news_resources.NewsListResource, '/api/v2/news')
    # для одного объекта
    api.add_resource(news_resources.NewsResource, '/api/v2/news/<int:news_id>')
    app.run()  # port=8080, host='127.0.0.1'


def add_user(email, password, name=None, about=None):
    db_sess = db_session.create_session()
    user = User()
    user.email = email
    user.hashed_password = User.get_password_hash(password)
    if name is not None:
        user.name = name
    if about is not None:
        user.about = about
    db_sess.add(user)
    db_sess.commit()


def tmp_fill_base():
    add_user("admin@email.com", "qwerty", "Админ", "биография пользователя 1")
    db_sess = db_session.create_session()
    news = News(title="Первая новость", content="Привет блог!",
                user_id=1, is_private=False)
    db_sess.add(news)
    db_sess.commit()


if __name__ == '__main__':
    main()
