#!/usr/bin/python
#-*- coding: UTF-8 -*-
import time

from ext import db
from flask_login import UserMixin


class TodoList(db.Model):
    __tablename__ = 'todolist'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(1024), nullable=False)
    status = db.Column(db.Integer, nullable=False)
    # create_time = db.Column(db.Integer, nullable=False)
    time = db.Column(db.String(1024),nullable=False)

    def __init__(self, user_id, title, status,t):
        self.user_id = user_id
        self.title = title
        self.status = status
        # self.create_time = int(time.time())
        # self.create_time = '123'
        self.time = str(t)


class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(24), nullable=False)
    password = db.Column(db.String(24), nullable=False)
    ident = db.Column(db.Integer,nullable=True)

    def __init__(self, username, password,ident):
        self.username = username
        self.password = password
        self.ident = ident
