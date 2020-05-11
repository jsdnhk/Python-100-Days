"""
抽象類 / 方法重寫 / 多態
實現一個工資結算系統 公司有三種類型的員工
- 部門經理固定月薪12000元/月
- 程序員按本月工作小時數每小時100元
- 銷售員1500元/月的底薪加上本月銷售額5%的提成
輸入員工的信息 輸出每位員工的月薪信息

Version: 0.1
Author: 駱昊
Date: 2018-03-12
"""

from abc import ABCMeta, abstractmethod


class Employee(object, metaclass=ABCMeta):

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_salary(self):
        pass


class Manager(Employee):

    # 想一想: 如果不定義構造方法會怎麼樣
    def __init__(self, name):
        # 想一想: 如果不調用父類構造器會怎麼樣
        super().__init__(name)

    def get_salary(self):
        return 12000


class Programmer(Employee):

    def __init__(self, name):
        super().__init__(name)

    def set_working_hour(self, working_hour):
        self._working_hour = working_hour

    def get_salary(self):
        return 100 * self._working_hour


class Salesman(Employee):

    def __init__(self, name):
        super().__init__(name)

    def set_sales(self, sales):
        self._sales = sales

    def get_salary(self):
        return 1500 + self._sales * 0.05


if __name__ == '__main__':
    emps = [Manager('武則天'), Programmer('狄仁傑'), Salesman('白元芳')]
    for emp in emps:
        if isinstance(emp, Programmer):
            working_hour = int(input('請輸入%s本月工作時間: ' % emp.name))
            emp.set_working_hour(working_hour)
        elif isinstance(emp, Salesman):
            sales = float(input('請輸入%s本月銷售額: ' % emp.name))
            emp.set_sales(sales)
        print('%s本月月薪爲: ￥%.2f元' % (emp.name, emp.get_salary()))
