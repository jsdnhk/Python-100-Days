"""
用戶身份驗證

Version: 0.1
Author: 駱昊
Date: 2018-02-28
"""
# import getpass
# from getpass import getpass
# from getpass import *

username = input('請輸入用戶名: ')
password = input('請輸入口令: ')
# 輸入口令的時候終端中沒有回顯
# password = getpass.getpass('請輸入口令: ')
if username == 'admin' and password == '123456':
    print('身份驗證成功!')
else:
    print('身份驗證失敗!')
