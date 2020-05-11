"""
多個線程共享數據 - 有鎖的情況

Version: 0.1
Author: 駱昊
Date: 2018-03-20
"""

import time
import threading


class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = threading.Lock()

    def deposit(self, money):
        # 獲得鎖後代碼才能繼續執行
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            time.sleep(0.01)
            self._balance = new_balance
        finally:
            # 操作完成後一定要記着釋放鎖
            self._lock.release()

    @property
    def balance(self):
        return self._balance


if __name__ == '__main__':
    account = Account()
    # 創建100個存款的線程向同一個賬戶中存錢
    for _ in range(100):
        threading.Thread(target=account.deposit, args=(1,)).start()
    # 等所有存款的線程都執行完畢
    time.sleep(2)
    print('賬戶餘額爲: ￥%d元' % account.balance)

# 想一想結果爲什麼不是我們期望的100元
