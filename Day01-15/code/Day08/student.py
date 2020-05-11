"""
定義和使用學生類

Version: 0.1
Author: 駱昊
Date: 2018-03-08
"""


def _foo():
    print('test')


class Student(object):

    # __init__是一個特殊方法用於在創建對象時進行初始化操作
    # 通過這個方法我們可以爲學生對象綁定name和age兩個屬性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在學習%s.' % (self.name, course_name))

    # PEP 8要求標識符的名字用全小寫多個單詞用下劃線連接
    # 但是很多程序員和公司更傾向於使用駝峯命名法(駝峯標識)
    def watch_av(self):
        if self.age < 18:
            print('%s只能觀看《熊出沒》.' % self.name)
        else:
            print('%s正在觀看島國大電影.' % self.name)


def main():
    stu1 = Student('駱昊', 38)
    stu1.study('Python程序設計')
    stu1.watch_av()
    stu2 = Student('王大錘', 15)
    stu2.study('思想品德')
    stu2.watch_av()


if __name__ == '__main__':
    main()
