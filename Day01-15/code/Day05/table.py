"""
輸出乘法口訣表(九九表)

Version: 0.1
Author: 駱昊
Date: 2018-03-02
"""

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()
