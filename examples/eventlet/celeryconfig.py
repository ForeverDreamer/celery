import os
import sys

# sys.path.insert(0, os.getcwd())

# ## Start worker with -P eventlet
# Never use the worker_pool setting as that'll patch
# the worker too late.

broker_url = 'amqp://guest:guest@localhost:5672//'
result_backend = os.getenv('CELERY_RESULT_BACKEND', 'redis://')
worker_disable_rate_limits = True
result_expires = 30 * 60

imports = (
    'examples.eventlet.tasks',
    'examples.eventlet.webcrawler'
)
