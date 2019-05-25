import time
import functools
from urllib.request import urlopen
from contextlib import ContextDecorator


class timeit(object):
    def __call__(self, f):
        @functools.wraps(f)
        def decorated(*args, **kwds):
            with self:
                return f(*args, **kwds)
        return decorated

    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, *args, **kw):
        elapsed = time.time() - self.start_time
        print("{:.3} sec".format(elapsed))


def cpu_bound(a, b):
    return a ** b


def io_bound(urls):
    data = []
    for url in urls:
        data.append(urlopen(url).read())
    return data


@timeit()
def simple_1(N, a, b):
    for i in range(N):
        cpu_bound(a, b)


@timeit()
def simple_2(N, urls):
    for i in range(N):
        io_bound(urls)


if __name__ == '__main__':
    a = 7777
    b = 200000
    urls = [
        "http://google.com",
        "http://yahoo.com",
        "http://linkedin.com",
        "http://facebook.com"
    ]
    simple_1(10, a, b)
    simple_2(10, urls)