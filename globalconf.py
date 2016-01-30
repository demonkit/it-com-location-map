#!/usr/bin/python
# -*- coding: utf-8 -*-


import os


BASE_DIR = os.path.dirname(
        os.path.abspath(__file__))


DATA_DIR = os.path.join(BASE_DIR, 'data')


# process celery configuration
BROKER = 'amqp://guest:guest@10.16.45.109:5672'
BACKEND = BROKER