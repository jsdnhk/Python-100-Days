"""
實現進程間的通信

Version: 0.1
Author: 駱昊
Date: 2018-03-20
"""
import multiprocessing
import os


def sub_task(queue):
    print('子進程進程號:', os.getpid())
    counter = 0
    while counter < 1000:
        queue.put('Pong')
        counter += 1


if __name__ == '__main__':
    print('當前進程號:', os.getpid())
    queue = multiprocessing.Queue()
    p = multiprocessing.Process(target=sub_task, args=(queue,))
    p.start()
    counter = 0
    while counter < 1000:
        queue.put('Ping')
        counter += 1
    p.join()
    print('子任務已經完成.')
    for _ in range(2000):
        print(queue.get(), end='')
