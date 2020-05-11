"""
學生考試成績表

Version: 0.1
Author: 駱昊
Date: 2018-03-06
"""


def main():
    names = ['關羽', '張飛', '趙雲', '馬超', '黃忠']
    subjs = ['語文', '數學', '英語']
    scores = [[0] * 3] * 5
    for row, name in enumerate(names):
        print('請輸入%s的成績' % name)
        for col, subj in enumerate(subjs):
            scores[row][col] = float(input(subj + ': '))
    print(scores)
#   for row, name in enumerate(names):
#       print('請輸入%s的成績' % name)
#       scores[row] = [None] * len(subjs)
#       for col, subj in enumerate(subjs):
#           score = float(input(subj + ': '))
#           scores[row][col] = score
#   print(scores)

if __name__ == '__main__':
    main()
