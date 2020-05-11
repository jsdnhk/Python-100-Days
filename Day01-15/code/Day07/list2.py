"""
列表常用操作
- 列表連接
- 獲取長度
- 遍歷列表
- 列表切片
- 列表排序
- 列表反轉
- 查找元素

Version: 0.1
Author: 駱昊
Date: 2018-03-06
"""


def main():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']
    # 循環遍歷列表元素
    for fruit in fruits:
        print(fruit.title(), end=' ')
    print()
    # 列表切片
    fruits2 = fruits[1:4]
    print(fruits2)
    # fruit3 = fruits  # 沒有複製列表只創建了新的引用
    fruits3 = fruits[:]
    print(fruits3)
    fruits4 = fruits[-3:-1]
    print(fruits4)
    fruits5 = fruits[::-1]
    print(fruits5)


if __name__ == '__main__':
    main()
