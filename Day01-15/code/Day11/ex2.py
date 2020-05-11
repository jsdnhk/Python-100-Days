"""
異常機制 - 處理程序在運行時可能發生的狀態

Version: 0.1
Author: 駱昊
Date: 2018-03-13
"""

input_again = True
while input_again:
    try:
        a = int(input('a = '))
        b = int(input('b = '))
        print('%d / %d = %f' % (a, b, a / b))
        input_again = False
    except (ValueError, ZeroDivisionError) as msg:
        print(msg)
