import re


def main():
    # 創建正則表達式對象 使用了前瞻和回顧來保證手機號前後不應該出現數字
    pattern = re.compile(r'(?<=\D)(1[38]\d{9}|14[57]\d{8}|15[0-35-9]\d{8}|17[678]\d{8})(?=\D)')
    sentence = '''
    重要的事情說8130123456789遍，我的手機號是13512346789這個靚號，
    不是15600998765，也是110或119，王大錘的手機號纔是15600998765。
    '''
    # 查找所有匹配並保存到一個列表中
    mylist = re.findall(pattern, sentence)
    print(mylist)
    print('--------華麗的分隔線--------')
    # 通過迭代器取出匹配對象並獲得匹配的內容
    for temp in pattern.finditer(sentence):
        print(temp.group())
    print('--------華麗的分隔線--------')
    # 通過search函數指定搜索位置找出所有匹配
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())


if __name__ == '__main__':
    main()
