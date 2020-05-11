"""
定義和使用集合

Version: 0.1
Author: 駱昊
Date: 2018-03-06
"""


def main():
    set1 = {1, 2, 3, 3, 3, 2}
    print(set1)
    print('Length =', len(set1))
    set2 = set(range(1, 10))
    print(set2)
    set1.add(4)
    set1.add(5)
    set2.update([11, 12])
    print(set1)
    print(set2)
    set2.discard(5)
    # remove的元素如果不存在會引發KeyError
    if 4 in set2:
        set2.remove(4)
    print(set2)
    # 遍歷集合容器
    for elem in set2:
        print(elem ** 2, end=' ')
    print()
    # 將元組轉換成集合
    set3 = set((1, 2, 3, 3, 2, 1))
    print(set3.pop())
    print(set3)


if __name__ == '__main__':
    main()
