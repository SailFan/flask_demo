# encoding: utf-8
# @Time    : 2021/5/19 11:33 下午
# @Author  : Sail
# @File    : views.py
# @Software: PyCharm
import hashlib
import json

from flask import Blueprint, request, redirect, url_for, flash
from flask_login import current_user, login_user, login_required, logout_user

from app import db
from app import login_manager
from app.user.models.User import MantisUserTable

login=Blueprint('login',__name__)

@login.route("/", methods=["GET"])
def index():
    return "this is user index page"




@login_manager.user_loader
def load_user(user_id):
    return MantisUserTable.query.get(int(user_id))


@login.route("/login_in", methods=["POST"])
def login_in():
    subject=json.loads(request.get_data(as_text=True))
    user = MantisUserTable.query.filter_by(username=subject.get("username")).first()
    if user is None or not user.password==hashlib.md5(subject.get("password").encode(encoding='UTF-8')).hexdigest():
        return "用户名或者密码不存在"
    login_user(user, remember=False)
    return "sucess"




@login.route("/login_out", methods=["GET","POST"])
@login_required
def exit():
    logout_user()
    return "logout success"


@login.route("/test_connect",methods=["GET","POST"])
@login_required
def test_connect():
    print(MantisUserTable.query.all())
    return "success"




