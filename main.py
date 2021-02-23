from markupsafe import escape
from flask import Flask, url_for
app = Flask(__name__)


@app.route('/')
def root():
    return 'Hello World and Python'


@app.route('/login', methods=['POST'])
def login():
    return 'Login successfully'


@app.route('/string/<a_string>')
def get_string(a_string):
    return 'String: %s' % escape(a_string)


@app.route('/int/<int:an_integer>')
def get_int(an_integer):
    return 'Int: %s' % escape(an_integer)


@app.route('/float/<float:a_float>')
def get_float(a_float):
    return 'Float: %s' % escape(a_float)


@app.route('/path/<path:sub_path>')
def get_path(sub_path):
    return 'Path: %s' % escape(sub_path)


@app.route('/uuid/<uuid:an_uuid>')
def get_uuid(an_uuid):
    return 'UUID: %s' % escape(an_uuid)


@app.route('/trailing/')
def get_trailing():
    return 'trailing'


@app.route('/non_trailing')
def get_non_trailing():
    return 'Not Found'


@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))


with app.test_request_context():
    print(url_for('root'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))


if __name__ == '__main__':
    app.run()

