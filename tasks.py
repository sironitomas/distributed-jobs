import time
from subprocess import PIPE, Popen

from celery import Celery

app = Celery()
app.config_from_object('celeryconfig')


@app.task
def add(x, y):
    # simulate lengthy computational task
    time.sleep(15)
    return x + y


@app.task
def count_system_processes():
    p1 = Popen(['ps', '-aux'], stdout=PIPE)
    p2 = Popen(['wc', '-l'], stdin=p1.stdout, stdout=PIPE)
    p1.stdout.close()
    process_count = p2.communicate()[0].decode().strip()
    print('There are {} running processes in the system'.format(process_count))
