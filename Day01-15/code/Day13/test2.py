import time
from threading import Thread, Lock


class Account(object):

    def __init__(self, balance=0):
        self._balance = balance
        self._lock = Lock()

    @property
    def balance(self):
        return self._balance

    def deposit(self, money):
        # 當多個線程同時訪問一個資源的時候 就有可能因爲競爭資源導致資源的狀態錯誤
        # 被多個線程訪問的資源我們通常稱之爲臨界資源 對臨界資源的訪問需要加上保護
        if money > 0:
            self._lock.acquire()
            try:
                new_balance = self._balance + money
                time.sleep(0.01)
                self._balance = new_balance
            finally:
                self._lock.release()


class AddMoneyThread(Thread):

    def __init__(self, account):
        super().__init__()
        self._account = account

    def run(self):
        self._account.deposit(1)


def main():
    account = Account(1000)
    tlist = []
    for _ in range(100):
        t = AddMoneyThread(account)
        tlist.append(t)
        t.start()
    for t in tlist:
        t.join()
    print('賬戶餘額: %d元' % account.balance)


if __name__ == '__main__':
    main()
