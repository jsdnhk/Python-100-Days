"""
aiohttp - 異步HTTP網絡訪問
異步I/O（異步編程）- 只使用一個線程（單線程）來處理用戶請求
用戶請求一旦被接納，剩下的都是I/O操作，通過多路I/O複用也可以達到併發的效果
這種做法與多線程相比可以讓CPU利用率更高，因爲沒有線程切換的開銷
Redis/Node.js - 單線程 + 異步I/O
Celery - 將要執行的耗時間的任務異步化處理
異步I/O事件循環 - uvloop
"""
import asyncio
import re

import aiohttp


async def fetch(session, url):
    async with session.get(url, ssl=False) as resp:
        return await resp.text()


async def main():
    pattern = re.compile(r'\<title\>(?P<title>.*)\<\/title\>')
    urls = ('https://www.python.org/',
            'https://git-scm.com/',
            'https://www.jd.com/',
            'https://www.taobao.com/',
            'https://www.douban.com/')
    async with aiohttp.ClientSession() as session:
        for url in urls:
            html = await fetch(session, url)
            print(pattern.search(html).group('title'))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
