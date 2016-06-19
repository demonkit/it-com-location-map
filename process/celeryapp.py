#!/usr/bin/python
# -*- coding: utf-8 -*-


from __future__ import absolute_import

from celery import Celery

from . import celeryconfig


app = Celery('process')

app.config_from_object(celeryconfig)


if __name__ == '__main__':
    app.start()
