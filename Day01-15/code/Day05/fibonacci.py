"""
輸出斐波那契數列的前20個數
1 1 2 3 5 8 13 21 ...

Version: 0.1
Author: 駱昊
Date: 2018-03-02
"""

a = 0
b = 1
for _ in range(20):
    a, b = b, a + b
    print(a, end=' ')
