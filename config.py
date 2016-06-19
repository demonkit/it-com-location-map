#!/usr/bin/python
# -*- coding: utf-8 -*-


import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


DATA_DIR = os.path.join(BASE_DIR, 'data')


# process celery configuration
BROKER = "amqp://10.16.45.109:55672//"
BACKEND = "amqp://10.16.45.109:55672//"


# database config
SQLALCHEMY_DATABASE_URI = "sqlite://%s/%s" % (BASE_DIR, "it_company.db")
