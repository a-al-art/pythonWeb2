from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    user = "Ученик Академии Яндекса"
    return render_template('index.html', title='Домашняя страница',
                           username=user)


@app.route('/second')
def second_page():
    return '''Second <p> page</p>'''


@app.route('/countdown')
def countdown():
    countdown_list = [str(x) for x in range(10, 0, -1)]
    countdown_list.append('Пуск!')
    return '</br>'.join(countdown_list)


@app.route('/image_sample')
def image():
    return f'''<img width=500pt src="{url_for('static', filename='img/owl.jpeg')}" 
           alt="сова">'''


@app.route('/sample_page')
def return_sample_page():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/styles.css')}" />
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                  <nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="index">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/image_sample">image_sample</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Pricing</a>
        </li>

        </li>
      </ul>
    </div>
  </div>
</nav>
                    <h1>Правильная HTML-страница</h1>
                    <p>(made in YAL)</p>
                     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
                       <div class="alert alert-primary" role="alert">
                      А мы тут компонентами Bootstrap балуемся
                  </body>
                </html>"""


#
# @app.route('/greeting/<username>')
# def greeting(username):
#     return f'''<!doctype html>
#                 <html lang="en">
#                   <head>
#                     <meta charset="utf-8">
#                     <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
#                    <link rel="stylesheet"
#                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
#                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
#                    crossorigin="anonymous">
#                     <title>Привет, {username}</title>
#                   </head>
#                   <body>
#                     <h1>Привет, {username}!</h1>
#                   </body>
#                 </html>'''
#
#

@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/styles.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Форма для регистрации в суперсекретной системе</h1>
                            <h2>(сверхсекретно)</h2>
                            <div>
                                <form class="login_form" method="post" enctype="multipart/form-data">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <input type="password" class="form-control" id="password" placeholder="Введите пароль" name="password">
                                    <div class="form-group">
                                        <label for="classSelect">В каком вы классе</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>7</option>
                                          <option>8</option>
                                          <option>9</option>
                                          <option>10</option>
                                          <option>11</option>
                                        </select>
                                     </div>
                                    <div class="form-group">
                                        <label for="about">Немного о себе</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готов быть добровольцем</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        try:
            print(request.form['email'])
            print(request.form['password'])
            print(request.form['class'])
            # print(request.form['file'])
            print(request.form['about'])
            print(request.form['accept'])
            print(request.form['sex'])
            f = request.files['file']
            with open(f'uploaded_file_{f.filename}', 'wb' ) as out_file:
                out_file.write(f.read())
            print(f.read())
            return "Форма отправлена <a href='form_sample'>Заполнить форму</a>"
        except Exception as e:
            print(e, type(e))
            return "Отправка не удалась <a href='form_sample'>Заполнить форму</a>"

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
