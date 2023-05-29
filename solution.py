from flask import Flask

app = Flask(__name__)


# BEGIN (write your solution here)
@app.route('/')
def welcome_hexlet():
    return "Welcome to Hexlet!"
# END

