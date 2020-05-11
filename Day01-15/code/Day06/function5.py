"""
函數的參數
- 位置參數
- 可變參數
- 關鍵字參數
- 命名關鍵字參數

Version: 0.1
Author: 駱昊
Date: 2018-03-05
"""


# 參數默認值
def f1(a, b=5, c=10):
    return a + b * 2 + c * 3


print(f1(1, 2, 3))
print(f1(100, 200))
print(f1(100))
print(f1(c=2, b=3, a=1))


# 可變參數
def f2(*args):
    sum = 0
    for num in args:
        sum += num
    return sum


print(f2(1, 2, 3))
print(f2(1, 2, 3, 4, 5))
print(f2())


# 關鍵字參數
def f3(**kw):
    if 'name' in kw:
        print('歡迎你%s!' % kw['name'])
    elif 'tel' in kw:
        print('你的聯繫電話是: %s!' % kw['tel'])
    else:
        print('沒找到你的個人信息!')


param = {'name': '駱昊', 'age': 38}
f3(**param)
f3(name='駱昊', age=38, tel='13866778899')
f3(user='駱昊', age=38, tel='13866778899')
f3(user='駱昊', age=38, mobile='13866778899')
