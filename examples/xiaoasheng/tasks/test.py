import time

from examples.xiaoasheng import app, logger
from examples.xiaoasheng.tasks.base import BaseTask


# @app.task
# def error_handler(request, exc, traceback):
#     logger.info(f'executing {request.name}...')
#     print('Task {0} raised exception: {1!r}\n{2!r}'.format(
#           request.id, exc, traceback))


@app.task(base=BaseTask, bind=True)
def error(self):
    logger.info(f'执行任务 {self.name}')
    raise KeyError('测试错误')
    # try:
    #     raise KeyError('测试错误')
    # except KeyError as exc:
    #     # raise self.retry(exc=exc, countdown=5)
    #     logger.error(str(exc))
    #     return str(exc)


@app.task(base=BaseTask, bind=True, time_limit=5, soft_time_limit=3)
def timeout(self, x, y):
    logger.info(f'执行任务 {self.name}: x={x}, y={y}')
    time.sleep(1)
    print('1秒。。。')
    time.sleep(5)
    print('5秒。。。')
    time.sleep(10)
    print('10秒。。。')


@app.task(base=BaseTask, bind=True)
def hello(self, params):
    logger.info(f'执行任务 {self.name}: params={params}')
