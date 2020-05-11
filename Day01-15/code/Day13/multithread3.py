"""
使用多線程的情況 - 模擬多個下載任務

Version: 0.1
Author: 駱昊
Date: 2018-03-20
"""

from random import randint
from time import time, sleep
import threading


class DownloadTask(threading.Thread):

    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('開始下載%s...' % self._filename)
        time_to_download = randint(5, 10)
        print('剩餘時間%d秒.' % time_to_download)
        sleep(time_to_download)
        print('%s下載完成!' % self._filename)


def main():
    start = time()
    # 將多個下載任務放到多個線程中執行
    # 通過自定義的線程類創建線程對象 線程啓動後會回調執行run方法
    thread1 = DownloadTask('Python從入門到住院.pdf')
    thread1.start()
    thread2 = DownloadTask('Peking Hot.avi')
    thread2.start()
    thread1.join()
    thread2.join()
    end = time()
    print('總共耗費了%.3f秒' % (end - start))


if __name__ == '__main__':
    main()

# 請注意通過threading.Thread創建的線程默認是非守護線程
