#!/usr/bin/python
# -*- coding: utf-8 -*-


from __future__ import absolute_import

from celery import Celery


app = Celery("process",
             broker="amqp://guest:guest@10.16.45.109:5672//",
             backend="amqp://guest:guest@10.16.45.109:5672//")
             # include=['process.tasks.fetch_company'])


# app.config_from_object("process.celeryconfig")


if __name__ == '__main__':
    app.start()
