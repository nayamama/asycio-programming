# For green thred, switching between threads only happy on I/O. Non-I/O threads will take control forever.
import gevent.monkey
from syc_programming import io_bound, cpu_bound, timeit

gevent.monkey.patch_all()

@timeit()
def green_threaded(n_threads, func, *args):
    jobs = []
    for _ in range(n_threads):
        jobs.append(gevent.spawn(func, *args))
    # ensure all jobs have finished execution
    gevent.wait(jobs)

if __name__ == '__main__':
    a = 7777
    b = 200000
    urls = [
        "http://google.com",
        "http://yahoo.com",
        "http://linkedin.com",
        "http://facebook.com"
    ]
    green_threaded(10, cpu_bound, a, b)
    green_threaded(10, io_bound, urls)