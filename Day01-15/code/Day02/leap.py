"""
輸入年份 如果是閏年輸出True 否則輸出False

Version: 0.1
Author: 駱昊
Date: 2018-02-27
"""

year = int(input('請輸入年份: '))
# 如果代碼太長寫成一行不便於閱讀 可以使用\或()折行
is_leap = (year % 4 == 0 and year % 100 != 0 or
           year % 400 == 0)
print(is_leap)
