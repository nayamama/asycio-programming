from multiprocessing import Process
from syc_programming import io_bound, cpu_bound, timeit


@timeit()
def multiprocessed(n_thread, func, *args):
    pros = []
    for _ in range(n_thread):
        p = Process(target=func, args=args)
        pros.append(p)

    # start the process
    for p in pros:
        p.start()

    # ensure all processes have finished
    for p in pros:
        p.join()

if __name__ == '__main__':
    a = 7777
    b = 200000
    urls = [
        "http://google.com",
        "http://yahoo.com",
        "http://linkedin.com",
        "http://facebook.com"
    ]
    multiprocessed(10, cpu_bound, a, b)
    multiprocessed(10, io_bound, urls)