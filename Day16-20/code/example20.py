"""
線程間通信（共享數據）非常簡單因爲可以共享同一個進程的內存
進程間通信（共享數據）比較麻煩因爲操作系統會保護分配給進程的內存
要實現多進程間的通信通常可以用系統管道、套接字、三方服務來實現
multiprocessing.Queue
守護線程 - daemon thread
守護進程 - firewalld / httpd / mysqld
在系統停機的時候不保留的進程 - 不會因爲進程還沒有執行結束而阻礙系統停止
"""
from threading import Thread
from time import sleep


def output(content):
    while True:
        print(content, end='')


def main():
    Thread(target=output, args=('Ping', ), daemon=True).start()
    Thread(target=output, args=('Pong', ), daemon=True).start()
    sleep(5)
    print('bye!')


if __name__ == '__main__':
    main()
