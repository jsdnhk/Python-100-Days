"""
使用多線程的情況 - 模擬多個下載任務

Version: 0.1
Author: 駱昊
Date: 2018-03-20
"""

from random import randint
from time import time, sleep
import atexit
import _thread


def download_task(filename):
    print('開始下載%s...' % filename)
    time_to_download = randint(5, 10)
    print('剩餘時間%d秒.' % time_to_download)
    sleep(time_to_download)
    print('%s下載完成!' % filename)


def shutdown_hook(start):
    end = time()
    print('總共耗費了%.3f秒.' % (end - start))


def main():
    start = time()
    # 將多個下載任務放到多個線程中執行
    thread1 = _thread.start_new_thread(download_task, ('Python從入門到住院.pdf',))
    thread2 = _thread.start_new_thread(download_task, ('Peking Hot.avi',))
    # 註冊關機鉤子在程序執行結束前計算執行時間
    atexit.register(shutdown_hook, start)


if __name__ == '__main__':
    main()

# 執行這裏的代碼會引發致命錯誤(不要被這個詞嚇到) 因爲主線程結束後下載線程再想執行就會出問題
# 需要說明一下 由於_thread模塊屬於比較底層的線程操作而且不支持守護線程的概念
# 在實際開發中會有諸多不便 因此我們推薦使用threading模塊提供的高級操作進行多線程編程
