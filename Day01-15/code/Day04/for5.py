"""
輸入兩個正整數計算最大公約數和最小公倍數

Version: 0.1
Author: 駱昊
Date: 2018-03-01
"""

x = int(input('x = '))
y = int(input('y = '))
if x > y:
    (x, y) = (y, x)
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公約數是%d' % (x, y, factor))
        print('%d和%d的最小公倍數是%d' % (x, y, x * y // factor))
        break
