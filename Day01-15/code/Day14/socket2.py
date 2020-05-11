"""
套接字 - 基於TCP協議創建時間客戶端

Version: 0.1
Author: 駱昊
Date: 2018-03-22
"""

from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(('localhost', 6789))
while True:
    data = client.recv(1024)
    if not data:
        break
    print(data.decode('utf-8'))
client.close()
