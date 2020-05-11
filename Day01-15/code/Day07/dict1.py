"""
定義和使用字典

Version: 0.1
Author: 駱昊
Date: 2018-03-06
"""


def main():
    scores = {'駱昊': 95, '白元芳': 78, '狄仁傑': 82}
    print(scores['駱昊'])
    print(scores['狄仁傑'])
    for elem in scores:
        print('%s\t--->\t%d' % (elem, scores[elem]))
    scores['白元芳'] = 65
    scores['諸葛王朗'] = 71
    scores.update(冷麪=67, 方啓鶴=85)
    print(scores)
    if '武則天' in scores:
        print(scores['武則天'])
    print(scores.get('武則天'))
    print(scores.get('武則天', 60))
    print(scores.popitem())
    print(scores.popitem())
    print(scores.pop('駱昊', 100))
    scores.clear()
    print(scores)


if __name__ == '__main__':
    main()
