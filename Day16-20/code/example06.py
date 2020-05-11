"""
編碼和解碼 - BASE64
0-9A-Za-z+/
1100 0101 1001 0011 0111 0110
00110001 00011001 00001101 00110110
base64
b64encode / b64decode
-------------------------------------
序列化和反序列化
序列化 - 將對象變成字節序列(bytes)或者字符序列(str) - 串行化/醃鹹菜
反序列化 - 把字節序列或者字符序列還原成對象
Python標準庫對序列化的支持：
json - 字符形式的序列化
pickle - 字節形式的序列化
dumps / loads
"""
import base64
import json
import redis

from example02 import Person


class PersonJsonEncoder(json.JSONEncoder):

    def default(self, o):
        return o.__dict__


def main():
    cli = redis.StrictRedis(host='120.77.222.217', port=6379, 
                            password='123123')
    data = base64.b64decode(cli.get('guido'))
    with open('guido2.jpg', 'wb') as file_stream:
        file_stream.write(data)
    # with open('guido.jpg', 'rb') as file_stream:
    #     result = base64.b64encode(file_stream.read())
    # cli.set('guido', result)
    # persons = [
    #     Person('駱昊', 39), Person('王大錘', 18),
    #     Person('白元芳', 25), Person('狄仁傑', 37)
    # ]
    # persons = json.loads(cli.get('persons'))
    # print(persons)
    # cli.set('persons', json.dumps(persons, cls=PersonJsonEncoder))


if __name__ == '__main__':
    main()

