import asyncio


async def fetch(host):
    """從指定的站點抓取信息(協程函數)"""
    print(f'Start fetching {host}\n')
    # 跟服務器建立連接
    reader, writer = await asyncio.open_connection(host, 80)
    # 構造請求行和請求頭
    writer.write(b'GET / HTTP/1.1\r\n')
    writer.write(f'Host: {host}\r\n'.encode())
    writer.write(b'\r\n')
    # 清空緩存區(發送請求)
    await writer.drain()
    # 接收服務器的響應(讀取響應行和響應頭)
    line = await reader.readline()
    while line != b'\r\n':
        print(line.decode().rstrip())
        line = await reader.readline()
    print('\n')
    writer.close()


def main():
    """主函數"""
    urls = ('www.sohu.com', 'www.douban.com', 'www.163.com')
    # 獲取系統默認的事件循環
    loop = asyncio.get_event_loop()
    # 用生成式語法構造一個包含多個協程對象的列表
    tasks = [fetch(url) for url in urls]
    # 通過asyncio模塊的wait函數將協程列表包裝成Task（Future子類）並等待其執行完成
    # 通過事件循環的run_until_complete方法運行任務直到Future完成並返回它的結果
    futures = asyncio.wait(tasks)
    print(futures, type(futures))
    loop.run_until_complete(futures)
    loop.close()


if __name__ == '__main__':
    main()
