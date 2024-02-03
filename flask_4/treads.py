import datetime
import time
from main import sum_
import random
import threading


def treading():
    array = [random.randint(1, 100) for x in range(1000000)]
    delta = len(array) // 5
    res = 0
    start = 0
    stop = delta + 1
    threads = []
    for i in range(5):
        t = threading.Thread(target=sum_, args=(array[start:stop],))
        start += delta
        stop += delta
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


if __name__ == '__main__':
    start_time = time.time()
    treading()
    print(time.time() - start_time)
