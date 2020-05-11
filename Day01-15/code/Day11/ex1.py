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
    except ValueError:
        print('請輸入整數')
    except ZeroDivisionError:
        print('除數不能爲0')
# 處理異常讓代碼不因異常而崩潰是一方面
# 更重要的是可以通過對異常的處理讓代碼從異常中恢復過來
