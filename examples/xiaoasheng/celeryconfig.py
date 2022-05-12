import os

# RabbitMQ
broker_url = os.getenv('CELERY_BROKER_URL', 'pyamqp://')
result_backend = os.getenv('CELERY_RESULT_BACKEND', 'redis://')
result_serializer = 'json'
result_expires = os.getenv('CELERY_RESULT_EXPIRES', 3600)
task_time_limit = 2
task_track_started = True
# celery_acks_late = True
task_serializer = 'json'
accept_content = ['json']
timezone = 'Asia/Shanghai'
enable_utc = True

imports = (
    'examples.xiaoasheng.tasks.test',
    # 'clr.tasks.misc',
    # 'clr.tasks.model',
    # 'clr.tasks.knowledgebase',
)

# MongoDB
mongo_uri = os.getenv(
        'MONGO_URI',
        'mongodb://localhost:27017/celery'
    )

# 本地django启动监听8000会跟测试服冲突导致异常
dj_uri = os.getenv('DJ_URI', 'http://localhost:8080')
