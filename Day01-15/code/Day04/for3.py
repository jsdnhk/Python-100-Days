"""
輸入非負整數n計算n!

Version: 0.1
Author: 駱昊
Date: 2018-03-01
"""

n = int(input('n = '))
result = 1
for x in range(1, n + 1):
    result *= x
print('%d! = %d' % (n, result))
