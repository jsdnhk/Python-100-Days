"""
用for循環實現1~100之間的偶數求和

Version: 0.1
Author: 駱昊
Date: 2018-03-01
"""

sum = 0
for x in range(2, 101, 2):
    sum += x
print(sum)
