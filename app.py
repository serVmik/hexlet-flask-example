import json
import math
from flask import (Flask, request, redirect, render_template, url_for,
                   flash, get_flashed_messages)
from tools.validate import validate_user, validate_course, validate_post
from tools.tools import search_user_by_term, add_id

from tools.calculator import calculate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'


@app.route('/')
def index():
    return render_template('index.html',)


@app.get('/calculator')
def get_calculator():
    return render_template('calculator.html')


@app.post('/calculator')
def post_calculator():
    result = calculate()
    return render_template('calculator.html', result=result)


@app.get('/temp')
def get_temp():
    return render_template('temp.html')


@app.get('/courses')
def courses_get():
    with open('./data/courses.json', 'r') as data:
        courses = json.load(data)
    messages = get_flashed_messages(with_categories=True)
    return render_template('courses/index.html',
                           courses=courses, messages=messages,)


@app.post('/courses')
def course_post():
    with open('./data/courses.json', 'r') as data:
        courses = json.load(data)
    # Извлекаем данные формы
    course = request.form.to_dict()
    # Проверяем корректность данных
    errors = validate_course(course)
    # Если возникли ошибки,
    # то устанавливаем код ответа в 422 и рендерим форму с указанием ошибок
    if errors:
        return render_template('courses/new.html',
                               course=course, errors=errors,), 422

    # Если данные корректны, то сохраняем, добавляем флеш и выполняем редирект
    course.update({'id': add_id(courses)})
    courses.append(course)
    with open('./data/courses.json', 'w') as data:
        json.dump(courses, data, ensure_ascii=False, indent=2)
    flash('Course Added', 'success')
    return redirect(url_for('courses_get'))


@app.route('/courses/new')
def course_new():
    course = {'title': '', 'paid': ''}
    errors = {}
    return render_template('courses/new.html', course=course, errors=errors,)


@app.route('/users')
def users_get():
    with open('./data/users.json', 'r') as data:
        users = json.load(data)
    massages = get_flashed_messages(with_categories=True)
    return render_template('users/index.html', users=users, messages=massages,)


@app.post('/users')
def users_post():
    with open('./data/users.json', 'r') as data:
        users = json.load(data)
    user = request.form.to_dict()
    errors = validate_user(user)
    if errors:
        return render_template('users/new.html', user=user, errors=errors,), 422

    user.update({'id': add_id(users)})
    users.append(user)
    with open('./data/users.json', 'w') as data:
        json.dump(users, data, ensure_ascii=False, indent=2)
    flash('User was added successfully', 'success')
    return redirect(url_for('users_get'))


@app.route('/user/<int:id_>')
def user_get(id_):
    with open('./data/users.json', 'r') as data:
        users = json.load(data)
    user = next(filter(lambda user_: user_.get('id') == id_, users))
    return render_template('users/show.html', user=user,)


@app.route('/users/new')
def user_new():
    user = {'name': '', 'email': ''}
    errors = {}
    return render_template('users/new.html', user=user, errors=errors,)


@app.route('/users/search')
def users_search():
    search = request.args.get('term', '')
    with open('./data/users.json', 'r') as data:
        users = json.load(data)

    if search:
        users_output = search_user_by_term(search, users)
    else:
        users_output = users

    return render_template('users/index.html',
                           users=users_output, search=search,)


@app.route('/posts/<slug>')
def post_get(slug):
    with open('./data/posts.json', 'r') as data:
        posts = json.load(data)
    filtered_posts = filter(lambda post_: post_['slug'] == slug, posts)
    post = next(filtered_posts, None)
    if not post:
        return 'Page not found', 404

    return render_template('posts/show.html', post=post,)


@app.get('/posts')
def posts_get():
    with open('./data/posts.json', 'r') as data:
        posts = json.load(data)
    limit = 5
    page = request.args.get('page', default=1, type=int)
    pages = len(posts) // limit + math.ceil(len(posts) % limit)
    offset = (page - 1) * limit
    slice_of_posts = posts[offset:page*limit]
    messages = get_flashed_messages(with_categories=True)
    return render_template('posts/index.html', slice_of_posts=slice_of_posts,
                           page=page, pages=pages, messages=messages,)


@app.post('/posts')
def posts_post():
    with open('./data/posts.json', 'r') as data:
        posts = json.load(data)
    post = request.form.to_dict()
    errors = validate_post(post)
    if errors:
        return render_template('posts/new.html', post=post, errors=errors,), 422

    post['id'] = add_id(posts)
    posts.append(post)
    with open('./data/posts.json', 'w') as data:
        json.dump(posts, data, ensure_ascii=False, indent=2)
    flash('Post has been created', 'success')
    return redirect(url_for('posts_get'))


@app.route('/posts/new')
def posts_new():
    post = {'title': '', 'body': ''}
    errors = {}
    return render_template('posts/new.html', post=post, errors=errors,)
