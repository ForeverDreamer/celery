import contextlib

import pymongo

from examples.xiaoasheng import app


@contextlib.contextmanager
def mongo_client():
    client = pymongo.MongoClient(app.conf['mongo_uri'])
    # print('clr数据库连接成功！')
    yield client
    client.close()
    # print('clr关闭数据库！')
