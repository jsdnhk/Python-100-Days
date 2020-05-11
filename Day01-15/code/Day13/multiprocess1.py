"""
使用Process類創建多個進程

Version: 0.1
Author: 駱昊
Date: 2018-03-20
"""

# 通過下面程序的執行結果可以證實 父進程在創建子進程時複製了進程及其數據結構
# 每個進程都有自己獨立的內存空間 所以進程之間共享數據只能通過IPC的方式


from multiprocessing import Process, Queue
from time import sleep


def sub_task(string, q):
    number = q.get()
    while number:
        print('%d: %s' % (number, string))
        sleep(0.001)
        number = q.get()


def main():
    q = Queue(10)
    for number in range(1, 11):
        q.put(number)
    Process(target=sub_task, args=('Ping', q)).start()
    Process(target=sub_task, args=('Pong', q)).start()


if __name__ == '__main__':
    main()
