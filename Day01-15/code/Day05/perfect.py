"""
找出1~9999之間的所有完美數
完美數是除自身外其他所有因子的和正好等於這個數本身的數
例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14

Version: 0.1
Author: 駱昊
Date: 2018-03-02
"""
import math

for num in range(1, 10000):
    result = 0
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            result += factor
            if factor > 1 and num // factor != factor:
                result += num // factor
    if result == num:
        print(num)
