"""
查找 - 順序查找和二分查找
算法：解決問題的方法（步驟）
評價一個算法的好壞主要有兩個指標：漸近時間複雜度和漸近空間複雜度，通常一個算法很難做到時間複雜度和空間複雜度都很低（因爲時間和空間是不可調和的矛盾）
表示漸近時間複雜度通常使用大O標記
O(c)：常量時間複雜度 - 哈希存儲 / 布隆過濾器
O(log_2 n)：對數時間複雜度 - 折半查找
O(n)：線性時間複雜度 - 順序查找
O(n * log_2 n)：- 對數線性時間複雜度 - 高級排序算法（歸併排序、快速排序）
O(n ** 2)：平方時間複雜度 - 簡單排序算法（冒泡排序、選擇排序、插入排序）
O(n ** 3)：立方時間複雜度 - Floyd算法 / 矩陣乘法運算
也稱爲多項式時間複雜度
O(2 ** n)：幾何級數時間複雜度 - 漢諾塔
O(3 ** n)：幾何級數時間複雜度
也稱爲指數時間複雜度
O(n!)：階乘時間複雜度 - 旅行經銷商問題 - NP
"""
from math import log2, factorial
from matplotlib import pyplot

import numpy


def seq_search(items: list, elem) -> int:
    """順序查找"""
    for index, item in enumerate(items):
        if elem == item:
            return index
    return -1


def bin_search(items, elem):
    """二分查找"""
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if elem > items[mid]:
            start = mid + 1
        elif elem < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1


def main():
    """主函數（程序入口）"""
    num = 6
    styles = ['r-.', 'g-*', 'b-o', 'y-x', 'c-^', 'm-+', 'k-d']
    legends = ['對數', '線性', '線性對數', '平方', '立方', '幾何級數', '階乘']
    x_data = [x for x in range(1, num + 1)]
    y_data1 = [log2(y) for y in range(1, num + 1)]
    y_data2 = [y for y in range(1, num + 1)]
    y_data3 = [y * log2(y) for y in range(1, num + 1)]
    y_data4 = [y ** 2 for y in range(1, num + 1)]
    y_data5 = [y ** 3 for y in range(1, num + 1)]
    y_data6 = [3 ** y for y in range(1, num + 1)]
    y_data7 = [factorial(y) for y in range(1, num + 1)]
    y_datas = [y_data1, y_data2, y_data3, y_data4, y_data5, y_data6, y_data7]
    for index, y_data in enumerate(y_datas):
        pyplot.plot(x_data, y_data, styles[index])
    pyplot.legend(legends)
    pyplot.xticks(numpy.arange(1, 7, step=1))
    pyplot.yticks(numpy.arange(0, 751, step=50))
    pyplot.show()


if __name__ == '__main__':
    main()
