"""
排序 - 冒泡排序、選擇排序、歸併排序、快速排序
冒泡排序 - O(n ** 2)：兩兩比較，大的下沉
35, 97, 12, 68, 55, 73, 81, 40
35, 12, 68, 55, 73, 81, 40, [97]
12, 35, 55, 68, 73, 40, [81]
12, 35, 55, 68, 40, [73]
...
選擇排序 - O(n ** 2)：每次從剩下元素中選擇最小
-----------------------------------------
歸併排序 - O(n * log_2 n) - 高級排序算法
35, 97, 12, 68, 55, 73, 81, 40
[35, 97, 12, 68], [55, 73, 81, 40]
[35, 97], [12, 68], [55, 73], [81, 40]
[35], [97], [12], [68], [55], [73], [81], [40]
[35, 97], [12, 68], [55, 73], [40, 81]
[12, 35, 68, 97], [40, 55, 73, 81]
[12, 35, 40, 55, 68, 73, 81, 97]
-----------------------------------------
快速排序 - 以樞軸爲界將列表中的元素劃分爲兩個部分，左邊都比樞軸小，右邊都比樞軸大
35, 97, 12, 68, 55, 73, 81, 40
35, 12, [40], 68, 55, 73, 81, 97
[12], 35, [40], 68, 55, 73, 81, [97]
[12], 35, [40], 55, [68], 73, 81, [97]
[12], 35, [40], 55, [68], 73, [81], [97]
"""


class Person(object):
    """人"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def __gt__(self, other):
    #     return self.name > other.name

    def __str__(self):
        return f'{self.name}: {self.age}'

    def __repr__(self):
        return self.__str__()


def select_sort(origin_items, comp=lambda x, y: x < y):
    """簡單選擇排序"""
    items = origin_items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items


# 函數的設計要儘量做到無副作用（不影響調用者）
# 9 1 2 3 4 5 6 7 8
# 9 2 3 4 5 6 7 8 1
# *前面的參數叫位置參數，傳參時只需要對號入座即可
# *後面的參數叫命名關鍵字參數，傳參時必須給出參數名和參數值
# *args - 可變參數 - 元組
# **kwargs - 關鍵字參數 - 字典
def bubble_sort(origin_items, *, comp=lambda x, y: x > y):
    """冒泡排序"""
    items = origin_items[:]
    for i in range(1, len(items)):
        swapped = False
        for j in range(i - 1, len(items) - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items) - i - 1, i - 1, -1):
                if comp(items[j - 1], items[j]):
                    items[j], items[j - 1] = items[j - 1], items[j]
                    swapped = True
        if not swapped:
            break
    return items


def merge_sort(items, comp=lambda x, y: x <= y):
    """歸併排序"""
    if len(items) < 2:
        return items[:]
    mid = len(items) // 2
    left = merge_sort(items[:mid], comp)
    right = merge_sort(items[mid:], comp)
    return merge(left, right, comp)


def merge(items1, items2, comp=lambda x, y: x <= y):
    """合併（將兩個有序列表合併成一個新的有序列表）"""
    items = []
    index1, index2 = 0, 0
    while index1 < len(items1) and index2 < len(items2):
        if comp(items1[index1], items2[index2]):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 1
    items += items1[index1:]
    items += items2[index2:]
    return items


def quick_sort(origin_items, comp=lambda x, y: x <= y):
    """快速排序"""
    items = origin_items[:]
    _quick_sort(items, 0, len(items) - 1, comp)
    return items


def _quick_sort(items, start, end, comp):
    """遞歸調用劃分和排序"""
    if start < end:
        pos = _partition(items, start, end, comp)
        _quick_sort(items, start, pos - 1, comp)
        _quick_sort(items, pos + 1, end, comp)


def _partition(items, start, end, comp):
    """劃分"""
    pivot = items[end]
    i = start - 1
    for j in range(start, end):
        if comp(items[j], pivot):
            i += 1
            items[i], items[j] = items[j], items[i]
    items[i + 1], items[end] = items[end], items[i + 1]
    return i + 1


def main():
    """主函數"""
    items = [35, 97, 12, 68, 55, 73, 81, 40]
    # print(bubble_sort(items))
    # print(select_sort(items))
    # print(merge_sort(items))
    print(quick_sort(items))
    items2 = [
        Person('Wang', 25), Person('Luo', 39),
        Person('Zhang', 50), Person('He', 20)
    ]
    # print(bubble_sort(items2, comp=lambda p1, p2: p1.age > p2.age))
    # print(select_sort(items2, comp=lambda p1, p2: p1.name < p2.name))
    # print(merge_sort(items2, comp=lambda p1, p2: p1.age <= p2.age))
    print(quick_sort(items2, comp=lambda p1, p2: p1.age <= p2.age))
    items3 = ['apple', 'orange', 'watermelon', 'durian', 'pear']
    # print(bubble_sort(items3))
    # print(bubble_sort(items3, comp=lambda x, y: len(x) > len(y)))
    # print(merge_sort(items3))
    print(merge_sort(items3))


if __name__ == '__main__':
    main()
