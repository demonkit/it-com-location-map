#!/usr/bin/python
# -*- coding: utf-8 -*-


from celery import Celery

from . import celeryconfig

app = Celery("grasp-data")

app.config_from_object(celeryconfig)