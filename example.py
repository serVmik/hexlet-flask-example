# 1. Импортируем класс-инициализатор Flask.
#    Его экземпляр и будет нашим WSGI-приложением:
from flask import Flask, render_template, request

users = ['mike', 'mishel', 'adel', 'keks', 'kamila']

# 2. Инстанцируем экземпляр, где класс принимает
#    первым аргументом имя модуля нашего приложения __name__
#    Это нужно, чтобы Flask знал, где искать шаблоны и статические файлы:
app = Flask(__name__)

# 3. Используем декоратор route(),
#    который связывает функцию-обработчик с конкретным адресом нашего сайта.
# @app.route('/')
# 4. Функция-обработчик возвращает ответ, который выведется в браузере:
# def hello_world():
#     return 'Welcome to Flask!'


@app.route('/')
def index():
    return render_template(
        'index.html',
    )


# @app.route('/data/users.json')
# def users():
#     pass


# @app.get('/users')
# def users_get():
#     return 'GET /users'


@app.route('/users')
def get_users():
    search = request.args.get('term', '')

    if search:
        users_output = search_user_by_term(search, users)
    else:
        users_output = users

    return render_template(
        'users/index.html',
        users_output=users_output,
        search=search,
    )


def search_user_by_term(search_func, users_func):
    result = []
    for user_func in users_func:
        if search_func in user_func:
            result.append(user_func)
    return result


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
