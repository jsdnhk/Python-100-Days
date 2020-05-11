"""
輸出2~99之間的素數

Version: 0.1
Author: 駱昊
Date: 2018-03-02
"""

import math

for num in range(2, 100):
    is_prime = True
    for factor in range(2, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')
