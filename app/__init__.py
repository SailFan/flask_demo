# encoding: utf-8
# @Time    : 2021/5/19 4:52 下午
# @Author  : Sail
# @File    : __init__.py.py
# @Software: PyCharm


# 实例化flask登录插件
import os

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import config
login_manager = LoginManager()
login_manager.login_view = "login.login_in"
login_manager.session_protection = 'strong'

db=SQLAlchemy()

def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    from app.user.views import login
    app.register_blueprint(login, url_prefix='/login')
    app.config.from_object(config.DevelopmentConfig)

    db.init_app(app)

    login_manager.init_app(app)


    @app.route('/')
    def hello():
        return 'Hello, World!'


    return app