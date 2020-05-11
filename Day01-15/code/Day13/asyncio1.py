"""
異步I/O操作 - asyncio模塊

Version: 0.1
Author: 駱昊
Date: 2018-03-21
"""

import asyncio
import threading
# import time


@asyncio.coroutine
def hello():
    print('%s: hello, world!' % threading.current_thread())
    # 休眠不會阻塞主線程因爲使用了異步I/O操作
    # 注意有yield from纔會等待休眠操作執行完成
    yield from asyncio.sleep(2)
    # asyncio.sleep(1)
    # time.sleep(1)
    print('%s: goodbye, world!' % threading.current_thread())


loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
# 等待兩個異步I/O操作執行結束
loop.run_until_complete(asyncio.wait(tasks))
print('game over!')
loop.close()
