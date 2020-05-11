"""
Python的內置函數
- 數學相關: abs / divmod / pow / round / min / max / sum
- 序列相關: len / range / next / filter / map / sorted / slice / reversed
- 類型轉換: chr / ord / str / bool / int / float / complex / bin / oct / hex
- 數據結構: dict / list / set / tuple
- 其他函數: all / any / id / input / open / print / type

Version: 0.1
Author: 駱昊
Date: 2018-03-05
"""


def myfilter(mystr):
    return len(mystr) == 6


# help()
print(chr(0x9a86))
print(hex(ord('駱')))
print(abs(-1.2345))
print(round(-1.2345))
print(pow(1.2345, 5))
fruits = ['orange', 'peach', 'durian', 'watermelon']
print(fruits[slice(1, 3)])
fruits2 = list(filter(myfilter, fruits))
print(fruits)
print(fruits2)
