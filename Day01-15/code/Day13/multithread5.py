"""
多個線程共享數據 - 沒有鎖的情況

Version: 0.1
Author: 駱昊
Date: 2018-03-20
"""

from time import sleep
from threading import Thread, Lock


class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        # 先獲取鎖才能執行後續的代碼
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            # 這段代碼放在finally中保證釋放鎖的操作一定要執行
            self._lock.release()

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def main():
    account = Account()
    threads = []
    # 創建100個存款的線程向同一個賬戶中存錢
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    # 等所有存款的線程都執行完畢∫
    for t in threads:
        t.join()
    print('賬戶餘額爲: ￥%d元' % account.balance)


if __name__ == '__main__':
    main()
