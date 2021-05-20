# encoding: utf-8
# @Time    : 2021/5/20 10:49 上午
# @Author  : Sail
# @File    : config.py
# @Software: PyCharm

import os

DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = 'HmElIsBkPKQNmfN2'
HOST = '192.168.2.92'
PORT = '3306'
DATABASE = 'qa_p'


class BaseConfig:
    SECRET_KEY = os.getenv('SECRET_KEY', 'some secret words')
    ITEMS_PER_PAGE = 10


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SQLALCHEMY_ECHO=True


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root:HmElIsBkPKQNmfN2@192.168.2.92:3306/qa_p?charset=utf8"



config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}