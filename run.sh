#!/usr/bin/env bash
celery worker -A process.celeryapp:app -l info --logfile=logs/process.log --pool=solo