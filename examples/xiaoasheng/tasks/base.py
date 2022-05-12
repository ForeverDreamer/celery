from celery import Task
from celery.worker.request import Request

from examples.xiaoasheng import logger


class BaseRequest(Request):
    """A minimal custom request to log failures and hard time limits."""

    def on_timeout(self, soft, timeout):
        super(BaseRequest, self).on_timeout(soft, timeout)
        if not soft:
            logger.warning(f'检测到任务超时：name={self.task.name}')

    def on_failure(self, exc_info, send_failed_event=True, return_ok=False):
        super().on_failure(
            exc_info,
            send_failed_event=send_failed_event,
            return_ok=return_ok
        )
        logger.warning(f'检测到任务失败：name={self.task.name}, send_failed_event={send_failed_event}, return_ok={return_ok}')


class BaseTask(Task):

    Request = BaseRequest

    def before_start(self, task_id, args, kwargs):
        logger.info(f'任务即将开始：task_id={task_id}, args={args}, kwargs={kwargs}')

    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        logger.info(f'任务返回：status={status}, retval={retval}, task_id={task_id}, args={args}, kwargs={kwargs}')
        # 可以存到日志分析系统
        # print(str(einfo))

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        logger.error(f'任务执行错误：exc={exc}, task_id={task_id}, args={args}, kwargs={kwargs}')

    def on_retry(self, exc, task_id, args, kwargs, einfo):
        logger.info(f'任务重试：exc={exc}, task_id={task_id}, args={args}, kwargs={kwargs}')

    def on_success(self, retval, task_id, args, kwargs):
        logger.info(f'任务执行成功：retval={retval}, task_id={task_id}, args={args}, kwargs={kwargs}')
