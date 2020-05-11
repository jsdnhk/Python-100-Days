"""
Craps賭博遊戲
玩家搖兩顆色子 如果第一次搖出7點或11點 玩家勝
如果搖出2點 3點 12點 莊家勝 其他情況遊戲繼續
玩家再次要色子 如果搖出7點 莊家勝
如果搖出第一次搖的點數 玩家勝
否則遊戲繼續 玩家繼續搖色子
玩家進入遊戲時有1000元的賭注 全部輸光遊戲結束

Version: 0.1
Author: 駱昊
Date: 2018-03-02
"""
from random import randint

money = 1000
while money > 0:
    print('你的總資產爲:', money)
    needs_go_on = False
    while True:
        debt = int(input('請下注: '))
        if 0 < debt <= money:
            break
    first = randint(1, 6) + randint(1, 6)
    print('玩家搖出了%d點' % first)
    if first == 7 or first == 11:
        print('玩家勝!')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('莊家勝!')
        money -= debt
    else:
        needs_go_on = True

    while needs_go_on:
        current = randint(1, 6) + randint(1, 6)
        print('玩家搖出了%d點' % current)
        if current == 7:
            print('莊家勝')
            money -= debt
            needs_go_on = False
        elif current == first:
            print('玩家勝')
            money += debt
            needs_go_on = False

print('你破產了, 遊戲結束!')
