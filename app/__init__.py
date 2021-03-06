import sys, os, logging
from flask import Flask, Blueprint
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_socketio import SocketIO
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from config import basedir_join


app      = Flask(__name__)
lm       = LoginManager(app)
bcrypt   = Bcrypt(app)
socketio = SocketIO(async_mode='gevent')
csrf     = CSRFProtect(app)
db       = SQLAlchemy(app)
main     = Blueprint('main', __name__, template_folder = 'templates',\
                                         static_folder = 'static')


def create_app(debug = False):
    app.debug     = debug
    lm.login_view = 'main.login'
    socketio.init_app(app)
    app.config.from_pyfile(basedir_join('config.py')['path'])
    app.register_blueprint(main)
    db.create_all()
    return app


from . import routes, events, models
