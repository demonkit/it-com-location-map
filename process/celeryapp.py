#!/usr/bin/python
# -*- coding: utf-8 -*-


from __future__ import absolute_import

from celery import Celery

import globalconf


app = Celery('process',
             broker=globalconf.BROKER,
             backend=globalconf.BACKEND,
             include=['process.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
)


if __name__ == '__main__':
    app.start()