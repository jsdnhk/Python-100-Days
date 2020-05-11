"""
字符串常用操作 - 實現字符串倒轉的方法

Version: 0.1
Author: 駱昊
Date: 2018-03-19
"""

from io import StringIO


def reverse_str1(str):
    return str[::-1]


def reverse_str2(str):
    if len(str) <= 1:
        return str
    return reverse_str2(str[1:]) + str[0:1]


def reverse_str3(str):
    # StringIO對象是Python中的可變字符串
    # 不應該使用不變字符串做字符串連接操作 因爲會產生很多無用字符串對象
    rstr = StringIO()
    str_len = len(str)
    for index in range(str_len - 1, -1, -1):
        rstr.write(str[index])
    return rstr.getvalue()


def reverse_str4(str):
    return ''.join(str[index] for index in range(len(str) - 1, -1, -1))


def reverse_str5(str):
    # 將字符串處理成列表
    str_list = list(str)
    str_len = len(str)
    # 使用zip函數將兩個序列合併成一個產生元組的迭代器
    # 每次正好可以取到一前一後兩個下標來實現元素的交換
    for i, j in zip(range(str_len // 2), range(str_len - 1, str_len // 2, -1)):
        str_list[i], str_list[j] = str_list[j], str_list[i]
    # 將列表元素連接成字符串
    return ''.join(str_list)


if __name__ == '__main__':
    str = 'I love Python'
    print(reverse_str1(str))
    print(str)
    print(reverse_str2(str))
    print(str)
    print(reverse_str3(str))
    print(str)
    print(reverse_str4(str))
    print(str)
    print(reverse_str5(str))
    print(str)
