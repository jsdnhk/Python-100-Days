"""
寫入CSV文件

Version: 0.1
Author: 駱昊
Date: 2018-03-13
"""

import csv


class Teacher(object):

    def __init__(self, name, age, title):
        self.__name = name
        self.__age = age
        self.__title = title
        self.__index = -1

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def title(self):
        return self.__title


filename = 'teacher.csv'
teachers = [Teacher('駱昊', 38, '叫獸'), Teacher('狄仁傑', 25, '磚家')]

try:
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        for teacher in teachers:
            writer.writerow([teacher.name, teacher.age, teacher.title])
except BaseException as e:
    print('無法寫入文件:', filename)
else:
    print('保存數據完成!')
