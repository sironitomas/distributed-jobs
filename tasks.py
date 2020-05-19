from celery import Celery
import time

app = Celery()
app.config_from_object('celeryconfig')

@app.task
def add(x, y):
    # simulate lengthy computational task
    time.sleep(15)
    return x + y
