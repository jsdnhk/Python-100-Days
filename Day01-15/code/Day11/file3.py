"""
寫文本文件
將100以內的素數寫入到文件中

Version: 0.1
Author: 駱昊
Date: 2018-03-13
"""

from math import sqrt


def is_prime(n):
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True


# 試一試有什麼不一樣
# with open('prime.txt', 'a') as f:
with open('prime.txt', 'w') as f:
    for num in range(2, 100):
        if is_prime(num):
            f.write(str(num) + '\n')
print('寫入完成!')
