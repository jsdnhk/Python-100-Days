"""
函數的定義和使用 - 求最大公約數和最小公倍數

Version: 0.1
Author: 駱昊
Date: 2018-03-05
"""


def gcd(x, y):
    if x > y:
        (x, y) = (y, x)
    for factor in range(x, 1, -1):
        if x % factor == 0 and y % factor == 0:
            return factor
    return 1


def lcm(x, y):
    return x * y // gcd(x, y)


print(gcd(15, 27))
print(lcm(15, 27))
