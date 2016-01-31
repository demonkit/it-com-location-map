#!/usr/bin/python
# -*- coding: utf-8 -*-


from flask.ext.sqlalchemy import SQLAlchemy


from display import app


db = SQLAlchemy(app)
