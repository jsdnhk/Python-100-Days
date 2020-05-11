"""
實例方法和類方法的應用

Version: 0.1
Author: 駱昊
Date: 2018-03-12
"""

from math import sqrt


class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    # 靜態方法
    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and c + a > b

    # 實例方法
    def perimeter(self):
        return self._a + self._b + self._c

    # 實例方法
    def area(self):
        p = self.perimeter() / 2
        return sqrt(p * (p - self._a) * (p - self._b) * (p - self._c))


if __name__ == '__main__':
    # 用字符串的split方法將字符串拆分成一個列表
    # 再通過map函數對列表中的每個字符串進行映射處理成小數
    a, b, c = map(float, input('請輸入三條邊: ').split())
    # 先判斷給定長度的三條邊能否構成三角形
    # 如果能才創建三角形對象
    if Triangle.is_valid(a, b, c):
        tri = Triangle(a, b, c)
        print('周長:', tri.perimeter())
        print('面積:', tri.area())
        # 如果傳入對象作爲方法參數也可以通過類調用實例方法
        # print('周長:', Triangle.perimeter(tri))
        # print('面積:', Triangle.area(tri))
        # 看看下面的代碼就知道其實二者本質上是一致的
        # print(type(tri.perimeter))
        # print(type(Triangle.perimeter))
    else:
        print('不能構成三角形.')
