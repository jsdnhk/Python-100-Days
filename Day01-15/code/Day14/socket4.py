"""
套接字 - 基於UDP協議創建Echo客戶端

Version: 0.1
Author: 駱昊
Date: 2018-03-22
"""

from socket import *

client = socket(AF_INET, SOCK_DGRAM)
while True:
    data_str = input('請輸入: ')
    client.sendto(data_str.encode('utf-8'), ('localhost', 6789))
    data, addr = client.recvfrom(1024)
    data_str = data.decode('utf-8')
    print('服務器迴應:', data_str)
    if data_str == 'bye':
        break
client.close()
