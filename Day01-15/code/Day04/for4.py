"""
輸入一個正整數判斷它是不是素數

Version: 0.1
Author: 駱昊
Date: 2018-03-01
"""
from math import sqrt

num = int(input('請輸入一個正整數: '))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素數' % num)
else:
    print('%d不是素數' % num)
