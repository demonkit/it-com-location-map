# it-com-location-map

## how to run celery worker
`celery worker -A process.celeryapp:app -l info --logfile=logs/process.log --pool=solo`