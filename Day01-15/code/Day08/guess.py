"""
面向對象版本的猜數字遊戲

Version: 0.1
Author: 駱昊
Date: 2018-03-08
"""

from random import randint


class GuessMachine(object):

    def __init__(self):
        self._answer = None
        self._counter = None
        self._hint = None

    def reset(self):
        self._answer = randint(1, 100)
        self._counter = 0
        self._hint = None

    def guess(self, your_answer):
        self._counter += 1
        if your_answer > self._answer:
            self._hint = '小一點'
        elif your_answer < self._answer:
            self._hint = '大一點'
        else:
            self._hint = '恭喜你猜對了'
            return True
        return False

    @property
    def counter(self):
        return self._counter

    @property
    def hint(self):
        return self._hint


if __name__ == '__main__':
    gm = GuessMachine()
    play_again = True
    while play_again:
        game_over = False
        gm.reset()
        while not game_over:
            your_answer = int(input('請輸入: '))
            game_over = gm.guess(your_answer)
            print(gm.hint)
        if gm.counter > 7:
            print('智商餘額不足!')
        play_again = input('再玩一次?(yes|no)') == 'yes'
