import json

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def users():
    with open('./users.json', 'r+') as repo:
        users_ = json.load(repo)
    return render_template(
        '/users/index.html',
        users=users_
    )


@app.route('/users/new.html')
def new_user():
    return render_template(
        '/users/new.html'
    )


@app.post('/users')
def users_post():
    user = request.form.to_dict()

    with open('./users.json', 'r') as repo:
        users_ = json.load(repo)
    users_.append(user)
    with open('./users.json', 'w') as repo:
        json.dump(users_, repo, ensure_ascii=False, indent=2)

    return render_template(
        'users/index.html',
        users=users_
    )
