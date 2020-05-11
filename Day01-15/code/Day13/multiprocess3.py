"""
創建進程調用其他程序

Version: 0.1
Author: 駱昊
Date: 2018-03-20
"""

import subprocess
import sys

def main():
    # 通過sys.argv獲取命令行參數
    if len(sys.argv) > 1:
        # 第一個命令行參數是程序本身所以從第二個開始取
        for index in range(1, len(sys.argv)):
            try:
                # 通過subprocess模塊的call函數啓動子進程
                status = subprocess.call(sys.argv[index])
            except FileNotFoundError:
                print('不能執行%s命令' % sys.argv[index])
    else:
        print('請使用命令行參數指定要執行的進程')


if __name__ == '__main__':
    main()
