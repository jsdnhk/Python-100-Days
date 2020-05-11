"""
生成列表
- 用range創建數字列表
- 生成表達式
- 生成器

Version: 0.1
Author: 駱昊
Date: 2018-03-06
"""


# 生成Fibonacci序列的生成器
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    # 用range創建數值列表
    list1 = list(range(1, 11))
    print(list1)
    # 生成表達式
    list2 = [x * x for x in range(1, 11)]
    print(list2)
    list3 = [m + n for m in 'ABCDEFG' for n in '12345']
    print(list3)
    print(len(list3))
    # 生成器(節省空間但生成下一個元素時需要花費時間)
    gen = (m + n for m in 'ABCDEFG' for n in '12345')
    print(gen)
    for elem in gen:
        print(elem, end=' ')
    print()
    gen = fib(20)
    print(gen)
    for elem in gen:
        print(elem, end=' ')
    print()


if __name__ == '__main__':
    main()
