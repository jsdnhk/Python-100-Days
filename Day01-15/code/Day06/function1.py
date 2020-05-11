"""
函數的定義和使用 - 計算組合數C(7,3)

Version: 0.1
Author: 駱昊
Date: 2018-03-05
"""


# 將求階乘的功能封裝成一個函數
def factorial(n):
    result = 1
    for num in range(1, n + 1):
        result *= num
    return result


print(factorial(7) // factorial(3) // factorial(4))
