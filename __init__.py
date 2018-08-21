import os

from flask import Flask


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

    from . import auth, db
    db.init_app(app)
    app.register_blueprint(auth.bp)
    return app
