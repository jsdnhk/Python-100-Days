"""
加密和解密
對稱加密 - 加密和解密是同一個密鑰 - DES / AES
非對稱加密 - 加密和解密是不同的密鑰 - RSA
pip install pycrypto
"""
import base64

from hashlib import md5

from Crypto.Cipher import AES
from Crypto import Random
from Crypto.PublicKey import RSA

# # AES加密的密鑰（長度32個字節）
# key = md5(b'1qaz2wsx').hexdigest()
# # AES加密的初始向量（隨機生成）
# iv = Random.new().read(AES.block_size)


def main():
    """主函數"""
    # 生成密鑰對
    key_pair = RSA.generate(1024)
    # 導入公鑰
    pub_key = RSA.importKey(key_pair.publickey().exportKey())
    # 導入私鑰
    pri_key = RSA.importKey(key_pair.exportKey())
    message1 = 'hello, world!'
    # 加密數據
    data = pub_key.encrypt(message1.encode(), None)
    # 對加密數據進行BASE64編碼
    message2 = base64.b64encode(data[0])
    print(message2)
    # 對加密數據進行BASE64解碼
    data = base64.b64decode(message2)
    # 解密數據
    message3 = pri_key.decrypt(data)
    print(message3.decode())
    # # AES - 對稱加密
    # str1 = '我愛你們！'
    # cipher = AES.new(key, AES.MODE_CFB, iv)
    # # 加密
    # str2 = cipher.encrypt(str1)
    # print(str2)
    # # 解密
    # cipher = AES.new(key, AES.MODE_CFB, iv)
    # str3 = cipher.decrypt(str2)
    # print(str3.decode())


if __name__ == '__main__':
    main()
