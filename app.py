from flask import request, redirect, url_for,render_template

from .db import db_session


@app.route('/')
def home():
    render_template('index.html')


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


@app.route('/updateip', methods=['GET', 'POST'])
def updateip():
    int = "null"
    ip = "0.0.0.0"
    if request.method == 'POST':
        # interface = request.form['interface']
        # ip = request.form['myip']
        interface = request.args['interface']
        ip = request.args['myip']
    else:
        interface = request.args['interface'] + "in else"
        ip = request.args['myip']

    return interface, ip


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

