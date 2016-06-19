#!/usr/bin/python
# -*- coding: utf-8 -*-


from kombu import Queue


BROKER_URL = 'amqp://guest:guest@10.16.45.109:5672//'


CELERY_INCLUDE = ('process.tasks', )


CELERY_ENABLE_UTC = True

CELERY_TIMEZONE = "Asia/Shanghai"

CELERY_ROUTES = {
        'process.tasks.fetch_company': {
            'queue': 'process.tasks.fetch_company',
            'routing_key': 'process.tasks.fetch_company',
        },
}

CELERY_QUEUES = (
    Queue("process.tasks.fetch_company",
          routing_key="process.tasks.fetch_company"),
)
