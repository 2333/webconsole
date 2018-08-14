from flask import request, redirect, url_for


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

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.debug)
