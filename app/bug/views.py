# encoding: utf-8
# @Time    : 2021/5/19 11:34 下午
# @Author  : Sail
# @File    : views.py
# @Software: PyCharm
from flask import Blueprint

bug=Blueprint('bug',__name__)



@bug.route("/index/", methods=["GET"])
def home():
    return "this is bug page"

#
#
# @bug.route("/", methods=["GET"])
# def index():
#     return "this is index page"