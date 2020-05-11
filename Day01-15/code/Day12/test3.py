"""
驗證輸入用戶名和QQ號是否有效並給出對應的提示信息

要求：
用戶名必須由字母、數字或下劃線構成且長度在6~20個字符之間
QQ號是5~12的數字且首位不能爲0
"""

import re


def main():
    username = input('請輸入用戶名: ')
    qq = input('請輸入QQ號: ')
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
    if not m1:
        print('請輸入有效的用戶名.')
    m2 = re.match(r'^[1-9]\d{4,11}$', qq)
    if not m2:
        print('請輸入有效的QQ號.')
    if m1 and m2:
        print('你輸入的信息是有效的!')


if __name__ == '__main__':
    main()
