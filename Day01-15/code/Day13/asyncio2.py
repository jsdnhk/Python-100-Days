"""
異步I/O操作 - async和await

Version: 0.1
Author: 駱昊
Date: 2018-03-21
"""
import asyncio
import threading


# 通過async修飾的函數不再是普通函數而是一個協程
# 注意async和await將在Python 3.7中作爲關鍵字出現
async def hello():
    print('%s: hello, world!' % threading.current_thread())
    await asyncio.sleep(2)
    print('%s: goodbye, world!' % threading.current_thread())


loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
# 等待兩個異步I/O操作執行結束
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
