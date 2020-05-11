"""
雙色球隨機選號程序

Version: 0.1
Author: 駱昊
Date: 2018-03-06
"""

from random import randrange, randint, sample


def display(balls):
    """
    輸出列表中的雙色球號碼
    """
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('%02d' % ball, end=' ')
    print()


def random_select():
    """
    隨機選擇一組號碼
    """
    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    for _ in range(6):
        index = randrange(len(red_balls))
        selected_balls.append(red_balls[index])
        del red_balls[index]
    # 上面的for循環也可以寫成下面這行代碼
    # sample函數是random模塊下的函數
    # selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1, 16))
    return selected_balls


def main():
    n = int(input('機選幾注: '))
    for _ in range(n):
        display(random_select())


if __name__ == '__main__':
    main()
