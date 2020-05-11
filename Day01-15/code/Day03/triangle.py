"""
判斷輸入的邊長能否構成三角形
如果能則計算出三角形的周長和麪積

Version: 0.1
Author: 駱昊
Date: 2018-02-28
"""
import math

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print('周長: %f' % (a + b + c))
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('面積: %f' % (area))
else:
    print('不能構成三角形')
