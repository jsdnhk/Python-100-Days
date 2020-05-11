"""
猜數字遊戲
計算機出一個1~100之間的隨機數由人來猜
計算機根據人猜的數字分別給出提示大一點/小一點/猜對了

Version: 0.1
Author: 駱昊
Date: 2018-03-02
"""
import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('請輸入: '))
    if number < answer:
        print('大一點')
    elif number > answer:
        print('小一點')
    else:
        print('恭喜你猜對了!')
        break
print('你總共猜了%d次' % counter)
if counter > 7:
    print('你的智商餘額明顯不足')
