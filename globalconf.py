#!/usr/bin/python
# -*- coding: utf-8 -*-


import os


BASE_DIR = os.path.dirname(
        os.path.abspath(__file__))


DATA_DIR = os.path.join(BASE_DIR, 'data')


# process celery configuration
BROKER = 'amqp://localhost:5672'
BACKEND = BROKER
