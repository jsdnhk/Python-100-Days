"""
引發異常和異常棧

Version: 0.1
Author: 駱昊
Date: 2018-03-13
"""


def f1():
    raise AssertionError('發生異常')


def f2():
    f1()


def f3():
    f2()


f3()
