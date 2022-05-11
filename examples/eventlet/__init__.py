import os
import sys

# sys.path.insert(0, os.getcwd())

from celery import Celery
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

app = Celery('eventlet')
app.config_from_object('examples.eventlet.celeryconfig')
