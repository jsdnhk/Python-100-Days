"""
將華氏溫度轉換爲攝氏溫度
F = 1.8C + 32

Version: 0.1
Author: 駱昊
Date: 2018-02-27
"""

f = float(input('請輸入華氏溫度: '))
c = (f - 32) / 1.8
print('%.1f華氏度 = %.1f攝氏度' % (f, c))
