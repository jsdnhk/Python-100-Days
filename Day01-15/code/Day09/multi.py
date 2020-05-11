"""
多重繼承
- 通過多重繼承可以給一個類的對象具備多方面的能力
- 這樣在設計類的時候可以避免設計太多層次的複雜的繼承關係

Version: 0.1
Author: 駱昊
Date: 2018-03-12
"""


class Father(object):

    def __init__(self, name):
        self._name = name

    def gamble(self):
        print('%s在打麻將.' % self._name)

    def eat(self):
        print('%s在大吃大喝.' % self._name)


class Monk(object):

    def __init__(self, name):
        self._name = name

    def eat(self):
        print('%s在吃齋.' % self._name)

    def chant(self):
        print('%s在念經.' % self._name)


class Musician(object):

    def __init__(self, name):
        self._name = name

    def eat(self):
        print('%s在細嚼慢嚥.' % self._name)

    def play_piano(self):
        print('%s在彈鋼琴.' % self._name)


# 試一試下面的代碼看看有什麼區別
# class Son(Monk, Father, Musician):
# class Son(Musician, Father, Monk):


class Son(Father, Monk, Musician):

    def __init__(self, name):
        Father.__init__(self, name)
        Monk.__init__(self, name)
        Musician.__init__(self, name)


son = Son('王大錘')
son.gamble()
# 調用繼承自Father的eat方法
son.eat()
son.chant()
son.play_piano()
