# 1. Импортируем класс-инициализатор Flask.
#    Его экземпляр и будет нашим WSGI-приложением:
from flask import Flask, render_template

# 2. Инстанцируем экземпляр, где класс принимает
#    первым аргументом имя модуля нашего приложения __name__
#    Это нужно, чтобы Flask знал, где искать шаблоны и статические файлы:
app = Flask(__name__)


# 3. Используем декоратор route(),
#    который связывает функцию-обработчик с конкретным адресом нашего сайта.
@app.route('/')
# 4. Функция-обработчик возвращает ответ, который выведется в браузере:
def hello_world():
    return 'Welcome to Flask!'


# @app.route('/')
# def index():
#     pass


# @app.route('/data/users.json')
# def users():
#     pass


# @app.get('/users')
# def users_get():
#     return 'GET /users'


# @app.post('/users')
# def users():
#     return 'Users', 302


@app.route('/courses/<id_>')
def courses(id_):
    return f'Course id: {id_}'


@app.route('/users/<int:id_>')
def user(id_):
    return render_template(
        'users/show.html',
        name=id_,
        user=user
    )


# @app.errorhandler(404)
# def not_found(error):
#     return 'Oops!', 404
