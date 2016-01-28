#!/usr/bin/python
# -*- coding: utf-8 -*-


from __future__ import absolute_import

from celery import Celery


app = Celery('process',
             broker='amqp://guest:guest@10.16.45.109:5672',
             # backend='amqp://guest:guest@10.16.45.109:5672',
             include=['process.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
    CELERY_RESULT_BACKEND='amqp://guest:guest@10.16.45.109:5672'
)


if __name__ == '__main__':
    app.start()