# celeryapp.py

from celery import Celery

# use rabbitmq as broker
#app = Celery('tasks',
#    broker='amqp://celery_user:b3stp@ssev@@localhost:5672/celery_vhost',
#    backend='rpc://')

# use redis as broker
app = Celery('tasks',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0')