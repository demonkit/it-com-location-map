# it-com-location-map

## how to run celery worker

In windows:
`celery worker -A process.celeryapp:app -l info --logfile=logs/process.log --pool=solo`

In unix/linux:
`celery worker -A process.celeryapp:app -l info --logfile=logs/process.log`