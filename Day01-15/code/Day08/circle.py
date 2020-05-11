"""
練習
修一個游泳池 半徑(以米爲單位)在程序運行時輸入 游泳池外修一條3米寬的過道
過道的外側修一圈圍牆 已知過道的造價爲25元每平米 圍牆的造價爲32.5元每米
輸出圍牆和過道的總造價分別是多少錢(精確到小數點後2位)

Version: 0.1
Author: 駱昊
Date: 2018-03-08
"""

import math


class Circle(object):

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        self._radius = radius if radius > 0 else 0

    @property
    def perimeter(self):
        return 2 * math.pi * self._radius

    @property
    def area(self):
        return math.pi * self._radius * self._radius


if __name__ == '__main__':  
    radius = float(input('請輸入游泳池的半徑: '))
    small = Circle(radius)
    big = Circle(radius + 3)
    print('圍牆的造價爲: ￥%.1f元' % (big.perimeter * 115))
    print('過道的造價爲: ￥%.1f元' % ((big.area - small.area) * 65))
