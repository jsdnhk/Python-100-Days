"""
哈希摘要 - 數字簽名/指紋 - 單向哈希函數（沒有反函數不可逆）
應用領域：
1. 數據庫中的用戶敏感信息保存成哈希摘要
2. 給數據生成簽名驗證數據沒有被惡意篡改
3. 雲存儲服務的秒傳功能（去重功能）
"""


class StreamHasher():
    """摘要生成器"""

    def __init__(self, algorithm='md5', size=4096):
        """初始化方法
        @params:
            algorithm - 哈希摘要算法
            size - 每次讀取數據的大小
        """
        self.size = size
        cls = getattr(__import__('hashlib'), algorithm.lower())
        self.hasher = cls()
    

    def digest(self, file_stream):
        """生成十六進制的摘要字符串"""
        # data = file_stream.read(self.size)
        # while data:
        #     self.hasher.update(data)
        #     data = file_stream.read(self.size)
        for data in iter(lambda: file_stream.read(self.size), b''):
            self.hasher.update(data)
        return self.hasher.hexdigest()

    def __call__(self, file_stream):
        return self.digest(file_stream)


def main():
    """主函數"""
    hasher1 = StreamHasher()
    hasher2 = StreamHasher('sha1')
    hasher3 = StreamHasher('sha256')
    with open('Python-3.7.2.tar.xz', 'rb') as file_stream:
        print(hasher1.digest(file_stream))
        file_stream.seek(0, 0)
        print(hasher2.digest(file_stream))
        file_stream.seek(0, 0)
        print(hasher3(file_stream))


if __name__ == '__main__':
    main()
