import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'shjbxhud9280h1gx9eub9sugue'
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@10.16.45.109:3306/it_company"


class Static(object):
    LAGOU_WEBSITE = "http://www.lagou.com"