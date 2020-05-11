"""
對象之間的依賴關係和運算符重載

Version: 0.1
Author: 駱昊
Date: 2018-03-12
"""


class Car(object):

    def __init__(self, brand, max_speed):
        self._brand = brand
        self._max_speed = max_speed
        self._current_speed = 0

    @property
    def brand(self):
        return self._brand

    def accelerate(self, delta):
        self._current_speed += delta
        if self._current_speed > self._max_speed:
            self._current_speed = self._max_speed

    def brake(self):
        self._current_speed = 0

    def __str__(self):
        return '%s當前時速%d' % (self._brand, self._current_speed)


class Student(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    # 學生和車之間存在依賴關係 - 學生使用了汽車
    def drive(self, car):
        print('%s駕駛着%s歡快的行駛在去西天的路上' % (self._name, car._brand))
        car.accelerate(30)
        print(car)
        car.accelerate(50)
        print(car)
        car.accelerate(50)
        print(car)

    def study(self, course_name):
        print('%s正在學習%s.' % (self._name, course_name))

    def watch_av(self):
        if self._age < 18:
            print('%s只能觀看《熊出沒》.' % self._name)
        else:
            print('%s正在觀看島國愛情動作片.' % self._name)

    # 重載大於(>)運算符
    def __gt__(self, other):
        return self._age > other._age

    # 重載小於(<)運算符
    def __lt__(self, other):
        return self._age < other._age


if __name__ == '__main__':
    stu1 = Student('駱昊', 38)
    stu1.study('Python程序設計')
    stu1.watch_av()
    stu2 = Student('王大錘', 15)
    stu2.study('思想品德')
    stu2.watch_av()
    car = Car('QQ', 120)
    stu2.drive(car)
    print(stu1 > stu2)
    print(stu1 < stu2)
