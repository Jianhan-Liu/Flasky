"""
  Created by PyCharm.
  User: Liujianhan
  Date: 2019/4/12
  Time: 23:53
 """
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment
from flask_pagedown import PageDown

from .config import config

__author__ = 'liujianhan'

bootstrap = Bootstrap()
moment = Moment()
mail = Mail()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
pagedown = PageDown()

from blog.models import db


def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    # config[config_name].init_app(app)

    mail.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)
    pagedown.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all(app=app)

    from .main import main
    from .auth import auth
    app.register_blueprint(main)
    app.register_blueprint(auth, url_prefix='/auth')

    return app
