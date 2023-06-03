import json
from tools import validate
from flask import (
    Flask, request, redirect, render_template, url_for,
    flash, get_flashed_messages
)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'


@app.route('/')
def index():
    return render_template('index.html',)


@app.get('/courses')
def courses_get():
    with open('./data/courses.json', 'r') as data:
        courses = json.load(data)
    messages = get_flashed_messages(with_categories=True)
    return render_template('courses/index.html',
                           courses=courses, messages=messages,)


@app.post('/courses')
def course_post():
    course = request.form.to_dict()
    errors = validate.validate_course(course)
    if errors:
        return render_template('courses/new.html',
                               course=course, errors=errors,)

    with open('./data/courses.json', 'r') as data:
        courses = json.load(data)

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
    return render_template('courses/new.html',
                           course=course, errors=errors,)


@app.get('/users')
def users_get():
    with open('./data/users.json', 'r') as data:
        users = json.load(data)
    massages = get_flashed_messages(with_categories=True)
    return render_template('users/index.html',
                           users=users, messages=massages,)


@app.post('/users')
def user_post():
    user = request.form.to_dict()
    errors = validate.validate_user(user)
    if errors:
        return render_template('users/new.html',
                               user=user, errors=errors,)

    with open('./data/users.json', 'r') as data:
        users = json.load(data)
    user.update({'id': add_id(users)})
    users.append(user)
    with open('./data/users.json', 'w') as data:
        json.dump(users, data, ensure_ascii=False, indent=2)
    flash('User was added successfully', 'success')

    return redirect(url_for('users_get'))


@app.route('/users/new')
def user_new():
    user = {'name': '', 'email': ''}
    errors = {}
    return render_template('users/new.html',
                           user=user, errors=errors,)


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


def search_user_by_term(search, users):
    result = []
    for user in users:
        if search.lower() in user.get('name').lower():
            result.append(user)
    return result


def add_id(items):
    id = 1
    for item in items:
        if item.get('id', 1) >= id:
            id = item.get('id') + 1
    return id
