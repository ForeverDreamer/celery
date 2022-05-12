from pprint import pprint as pp


# python -m celery -A examples.app.myapp worker -P solo -l debug -n worker1@%h -E
def app_example():
    from examples.app.myapp import add
    print(add.name)
    print(add.delay(16, 16).get())


# python -m celery -A examples.eventlet worker -P solo -l debug -n worker1@%h -E
def eventlet_example():
    from examples.eventlet.tasks import urlopen
    from examples.eventlet.webcrawler import crawl
    print(urlopen.name)
    pp(urlopen.delay('https://www.baidu.com/').get())
    # print('----------------------------------------------')
    # print(crawl.name)
    # pp(crawl.delay('https://www.baidu.com/').get())


# python -m celery -A examples.app.myapp worker -P solo -l debug -n worker1@%h -E
def xiaoasheng_example():
    from examples.xiaoasheng.tasks.test import error, timeout, hello

    # print(error.delay())
    print(timeout.delay(5, 3))
    # print(hello.delay(params={'msg': '你好啊'}))
