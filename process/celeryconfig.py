#!/usr/bin/python
# -*- coding: utf-8 -*-


## Broker settings.
BROKER_URL = 'amqp://guest:guest@10.16.45.109:5672//'

# List of modules to import when celery starts.
CELERY_IMPORTS = ('process.tasks', )

## Using the database to store task state and results.
# CELERY_RESULT_BACKEND = 'db+sqlite:///results.db'


CELERY_ENABLE_UTC = True

CELERY_TIMEZONE = "Asia/Shanghai"
