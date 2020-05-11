"""
從文本文件中讀取數據

Version: 0.1
Author: 駱昊
Date: 2018-03-13
"""

import time


def main():
    # 一次性讀取整個文件內容
    with open('致橡樹.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    # 通過for-in循環逐行讀取
    with open('致橡樹.txt', mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    # 讀取文件按行讀取到列表中
    with open('致橡樹.txt') as f:
        lines = f.readlines()
    print(lines)
    

if __name__ == '__main__':
    main()
