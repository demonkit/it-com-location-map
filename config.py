#!/usr/bin/python
# -*- coding: utf-8 -*-


import os

import pro_conf


BASE_DIR = os.path.dirname(
        os.path.abspath(__file__))


DATA_DIR = os.path.join(BASE_DIR, 'data')


# process celery configuration
BROKER = pro_conf.BROKER
BACKEND = pro_conf.BACKEND
