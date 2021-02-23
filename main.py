from markupsafe import escape
from flask import Flask, url_for
app = Flask(__name__)


@app.route('/')
def root():
    return 'Hello World and Python'


@app.route('/login', methods=['POST'])
def login():
    return 'Login successfully'


if __name__ == '__main__':
    app.run()

