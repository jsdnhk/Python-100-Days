from socket import socket
from json import loads
from base64 import b64decode


def main():
    client = socket()
    client.connect(('192.168.1.2', 5566))
    # 定義一個保存二進制數據的對象
    in_data = bytes()
    # 由於不知道服務器發送的數據有多大每次接收1024字節
    data = client.recv(1024)
    while data:
        # 將收到的數據拼接起來
        in_data += data
        data = client.recv(1024)
    # 將收到的二進制數據解碼成JSON字符串並轉換成字典
    # loads函數的作用就是將JSON字符串轉成字典對象
    my_dict = loads(in_data.decode('utf-8'))
    filename = my_dict['filename']
    filedata = my_dict['filedata'].encode('utf-8')
    with open('/Users/Hao/' + filename, 'wb') as f:
        # 將base64格式的數據解碼成二進制數據並寫入文件
        f.write(b64decode(filedata))
    print('圖片已保存.')


if __name__ == '__main__':
    main()
