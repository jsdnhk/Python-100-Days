"""
裝飾器 - 裝飾器中放置的通常都是橫切關注（cross-concern）功能
所謂橫切關注功能就是很多地方都會用到但跟正常業務又邏輯沒有必然聯繫的功能
裝飾器實際上是實現了設計模式中的代理模式 - AOP（面向切面編程）
"""
from functools import wraps
from random import randint
from time import time, sleep

import pymysql


def record(output):

    def decorate(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time()
            ret_value = func(*args, **kwargs)
            output(func.__name__, time() - start)
            return ret_value

        return wrapper

    return decorate


def output_to_console(fname, duration):
    print('%s: %.3f秒' % (fname, duration))


def output_to_file(fname, duration):
    with open('log.txt', 'a') as file_stream:
        file_stream.write('%s: %.3f秒\n' % (fname, duration))


def output_to_db(fname, duration):
    con = pymysql.connect(host='localhost', port=3306,
                          database='test', charset='utf8',
                          user='root', password='123456',
                          autocommit=True)
    try:
        with con.cursor() as cursor:
            cursor.execute('insert into tb_record values (default, %s, %s)',
                           (fname, '%.3f' % duration))
    finally:
        con.close()


@record(output_to_console)
def random_delay(min, max):
    sleep(randint(min, max))


def main():
    for _ in range(3):
        # print(random_delay.__name__)
        random_delay(3, 5)
    # for _ in range(3):
    #     # 取消掉裝飾器
    #     random_delay.__wrapped__(3, 5)


if __name__ == '__main__':
    main()
