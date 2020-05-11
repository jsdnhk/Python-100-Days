"""
異常機制 - 處理程序在運行時可能發生的狀態

Version: 0.1
Author: 駱昊
Date: 2018-03-13
"""

import time
import sys

filename = input('請輸入文件名: ')
try:
    with open(filename) as f:
        lines = f.readlines()
except FileNotFoundError as msg:
    print('無法打開文件:', filename)
    print(msg)
except UnicodeDecodeError as msg:
    print('非文本文件無法解碼')
    sys.exit()
else:
    for line in lines:
        print(line.rstrip())
        time.sleep(0.5)
finally:
    # 此處最適合做善後工作
    print('不管發生什麼我都會執行')
