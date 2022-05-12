import os

from celery import Celery
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'examples.xiaoasheng.dj.settings')

app = Celery('xiaoasheng')
app.config_from_object('examples.xiaoasheng.celeryconfig')
