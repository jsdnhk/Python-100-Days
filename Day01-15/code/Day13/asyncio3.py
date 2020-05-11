"""
異步I/O操作 - asyncio模塊

Version: 0.1
Author: 駱昊
Date: 2018-03-21
"""
import asyncio


async def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    # 異步方式等待連接結果
    reader, writer = await connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    # 異步I/O方式執行寫操作
    await writer.drain()
    while True:
        # 異步I/O方式執行讀操作
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    writer.close()


loop = asyncio.get_event_loop()
# 通過生成式語法創建一個裝了三個協程的列表
hosts_list = ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']
tasks = [wget(host) for host in hosts_list]
# 下面的方法將異步I/O操作放入EventLoop直到執行完畢
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
