#!/usr/bin/python
# -*- coding: utf-8 -*-


from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

import config


app = Flask("display")
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True


db = SQLAlchemy(app)


import display.views
