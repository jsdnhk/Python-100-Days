"""
輸入學生考試成績計算平均分

Version: 0.1
Author: 駱昊
Date: 2018-03-06
"""


def main():
    number = int(input('請輸入學生人數: '))
    names = [None] * number
    scores = [None] * number
    for index in range(len(names)):
        names[index] = input('請輸入第%d個學生的名字: ' % (index + 1))
        scores[index] = float(input('請輸入第%d個學生的成績: ' % (index + 1)))
    total = 0
    for index in range(len(names)):
        print('%s: %.1f分' % (names[index], scores[index]))
        total += scores[index]
    print('平均成績是: %.1f分' % (total / number))


if __name__ == '__main__':
    main()
