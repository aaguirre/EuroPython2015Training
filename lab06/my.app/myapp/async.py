import gevent

def greenlet(fn):
    def wrapped(*args):
        g = gevent.Greenlet(fn, *args)
        g.start()
    return wrapped
