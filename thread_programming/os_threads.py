from threading import Thread
from syc_programming import io_bound, cpu_bound, timeit


@timeit()
def threaded(n_thread, func, *args):
    jobs = []
    for _ in range(n_thread):
        thread = Thread(target=func, args=args)
        jobs.append(thread)

    # start the thread
    for j in jobs:
        j.start()

    # ensure all threads have finished
    for j in jobs:
        j.join()

if __name__ == '__main__':
    a = 7777
    b = 200000
    urls = [
        "http://google.com",
        "http://yahoo.com",
        "http://linkedin.com",
        "http://facebook.com"
    ]
    threaded(10, cpu_bound, a, b)
    threaded(10, io_bound, urls)
