import asyncio
import time
import random


async def async_sum():
    array = [random.randint(1, 100) for x in range(1000000)]
    delta = len(array) // 5
    res = 0
    start = 0
    stop = delta + 1
    for _ in range(5):
        res += sum(array[start:stop])
        start += delta
        stop += delta
    print(res)


if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(async_sum())
    print(time.time() - start_time)
