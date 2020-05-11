"""
輸入學生考試成績計算平均分

Version: 0.1
Author: 駱昊
Date: 2018-03-06
"""

import os
import time


def main():
    str = 'Welcome to 1000 Phone Chengdu Campus      '
    while True:
        print(str)
        time.sleep(0.2)
        str = str[1:] + str[0:1]
        # for Windows use os.system('cls') instead
        os.system('clear')


if __name__ == '__main__':
    main()
