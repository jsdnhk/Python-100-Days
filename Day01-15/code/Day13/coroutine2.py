"""
使用協程 - 查看協程的狀態

Version: 0.1
Author: 駱昊
Date: 2018-03-21
"""

from time import sleep
from inspect import getgeneratorstate


def build_deliver_man(man_id):
    total = 0
    while True:
        total += 1
        print('%d號快遞員準備接今天的第%d單.' % (man_id, total))
        pkg = yield
        print('%d號快遞員收到編號爲%s的包裹.' % (man_id, pkg))
        sleep(0.5)


def package_center(deliver_man, max_per_day):
    num = 1
    # 創建狀態(GEN_CREATED) - 等待開始執行
    print(getgeneratorstate(deliver_man))
    deliver_man.send(None)
    # 掛起狀態(GEN_SUSPENDED) - 在yield表達式處暫停
    print(getgeneratorstate(deliver_man))
    # next(deliver_man)
    while num <= max_per_day:
        package_id = 'PKG-%d' % num
        deliver_man.send(package_id)
        num += 1
    deliver_man.close()
    # 結束狀態(GEN_CLOSED) - 執行完畢
    print(getgeneratorstate(deliver_man))
    print('今天的包裹派送完畢!')


dm = build_deliver_man(1)
package_center(dm, 10)
