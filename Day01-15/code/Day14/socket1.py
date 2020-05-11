"""
套接字 - 基於TCP協議創建時間服務器

Version: 0.1
Author: 駱昊
Date: 2018-03-22
"""

from socket import *
from time import *

server = socket(AF_INET, SOCK_STREAM)
server.bind(('localhost', 6789))
server.listen()
print('服務器已經啓動正在監聽客戶端連接.')
while True:
    client, addr = server.accept()
    print('客戶端%s:%d連接成功.' % (addr[0], addr[1]))
    currtime = localtime(time())
    timestr = strftime('%Y-%m-%d %H:%M:%S', currtime)
    client.send(timestr.encode('utf-8'))
    client.close()
server.close()
