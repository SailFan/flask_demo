# coding: utf-8
from flask_login import UserMixin

from app import db


class MantisUserTable(db.Model,UserMixin):
    __tablename__ = 'mantis_user_table'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(191), nullable=False, unique=True, server_default=db.FetchedValue())
    realname = db.Column(db.String(191), nullable=False, server_default=db.FetchedValue())
    email = db.Column(db.String(191), nullable=False, index=True, server_default=db.FetchedValue())
    password = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue())
    enabled = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue())
    protected = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    access_level = db.Column(db.SmallInteger, nullable=False, index=True, server_default=db.FetchedValue())
    login_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    lost_password_request_count = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    failed_login_count = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    cookie_string = db.Column(db.String(64), nullable=False, unique=True, server_default=db.FetchedValue())
    last_visit = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    date_created = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
