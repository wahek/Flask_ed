import multiprocessing
import time
from main import sum_
import random


def mult():
    array = [random.randint(1, 100) for x in range(1000000)]
    delta = len(array) // 5
    start = 0
    stop = delta + 1
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=sum_, args=(array[start:stop],))
        start += delta
        stop += delta
        processes.append(p)
        p.start()
    for p in processes:
        p.join()


if __name__ == '__main__':
    start_time = time.time()
    mult()
    print(time.time() - start_time)
    print("""Время по любому больше чем у потоков, плюс я не совсем понимаю как связать значения между собой так, как
    это разные программы, есть идея записывать в файл, но это неэффективно в любом случае""")
