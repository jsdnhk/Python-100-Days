"""
元組的定義和使用

Version: 0.1
Author: 駱昊
Date: 2018-03-06
"""


def main():
    # 定義元組
    t = ('駱昊', 38, True, '四川成都')
    print(t)
    # 獲取元組中的元素
    print(t[0])
    print(t[1])
    print(t[2])
    print(t[3])
    # 遍歷元組中的值
    for member in t:
        print(member)
    # 重新給元組賦值
    # t[0] = '王大錘'      # TypeError
    # 變量t重新引用了新的元組 原來的元組被垃圾回收
    t = ('王大錘', 20, True, '雲南昆明')
    print(t)
    # 元組和列表的轉換
    person = list(t)
    print(person)
    person[0] = '李小龍'
    person[1] = 25
    print(person)
    fruits_list = ['apple', 'banana', 'orange']
    fruits_tuple = tuple(fruits_list)
    print(fruits_tuple)
    print(fruits_tuple[1])


if __name__ == '__main__':
    main()