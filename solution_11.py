from flask import Flask, render_template, request

from data import generate_users

users = generate_users(100)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# BEGIN (write your solution here)
@app.route('/users')
def get_users():
    def search_user_by_term(search_func, users_func):
        result = []
        for user_func in users_func:
            first_name = user_func.get('first_name')
            if first_name.lower().startswith(search_func.lower()):
                result.append(first_name)
        return result

    search = request.args.get('term', '')
    users_output = search_user_by_term(search, users)

    return render_template(
        'users/index.html',
        users_output=users_output,
        search=search,
    )
# END
