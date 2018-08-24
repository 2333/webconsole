import os

from flask import Flask, request, redirect, url_for, render_template
from .db import db_session

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=""
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # ensure the instance folder exits
    try:
        os.makedirs(app.instance_path)
    except(OSError):
        pass

    # from . import auth, db
    # db.init_app(app)
    # app.register_blueprint(auth.bp)

    # Define some routers via tutorial
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/form<num>/')
    def form(num=None):
        if num:
            return render_template('form%s.html' % num)
        return url_for('index')

    @app.route('/table<num>/')
    def table(num=None):
        if num:
            return render_template('table%s.html' % num)
        return url_for('index')


    @app.route('/ppp/')
    def people():
        name = request.args.get('name')
        if not name:
            return redirect(url_for('login'))
        user_agent = request.headers.get('User-Agent')
        return 'Name: {0}; UA: {1}'.format(name, user_agent)


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

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)