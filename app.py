from flask import Flask, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello World!'


@app.route('/ppp/')
def people():
    name = request.args.get('name')
    if not name:
        return redirect(url_for('login'))
    user_agent = request.headers.get('User-Agent')
    return 'Name: {0}; UA: {1}'.format(name, user_agent)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        return 'User: {} login'.format(user_id)
    else:
        return 'Open Login Page'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.debug)
