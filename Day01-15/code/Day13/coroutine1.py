"""
使用協程 - 模擬快遞中心派發快遞

Version: 0.1
Author: 駱昊
Date: 2018-03-21
"""

from time import sleep
from random import random


def build_deliver_man(man_id):
    total = 0
    while True:
        total += 1
        print('%d號快遞員準備接今天的第%d單.' % (man_id, total))
        pkg = yield
        print('%d號快遞員收到編號爲%s的包裹.' % (man_id, pkg))
        sleep(random() * 3)


def package_center(deliver_man, max_per_day):
    num = 1
    deliver_man.send(None)
    # next(deliver_man)
    while num <= max_per_day:
        package_id = 'PKG-%d' % num
        deliver_man.send(package_id)
        num += 1
        sleep(0.1)
    deliver_man.close()
    print('今天的包裹派送完畢!')


dm = build_deliver_man(1)
package_center(dm, 10)

# 兩個函數雖然沒有調用關係但是創建快遞員的函數作爲一個協程協助了快遞中心函數完成任務
# 想一想如果有多個快遞員的時候應該如何處理
