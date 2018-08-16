from flask import Flask


def create_app():
    app = Flask(__name__)

    from . import auth, db
    db.init_app(app)
    app.register_blueprint(auth.bp)
    return app
