from celery import task
import time
import gevent

@task
def add(*args):
    time.sleep(30)
    return args[0] + args[1]

@task
def async():
    b = time.time()
    p = []
    for i in range(6):
        p.append(gevent.spawn(add, i, i))
    gevent.joinall(p)
    e = time.time()
    print 'async cost time: %s' % (e-b)

@task
def sync():
    b = time.time()
    for i in range(6):
        add(i, i)
    e = time.time()
    print 'sync cost time: %s' % (e-b)
