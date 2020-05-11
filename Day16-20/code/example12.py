"""
面向對象的三大支柱：封裝、繼承、多態
面向對象的設計原則：SOLID原則
面向對象的設計模式：GoF設計模式（單例、工廠、代理、策略、迭代器）
月薪結算系統 - 部門經理每月15000 程序員每小時200 銷售員1800底薪加銷售額5%提成
"""
from abc import ABCMeta, abstractmethod


class Employee(metaclass=ABCMeta):
    """員工(抽象類)"""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        """結算月薪(抽象方法)"""
        pass


class Manager(Employee):
    """部門經理"""

    def get_salary(self):
        return 15000.0


class Programmer(Employee):
    """程序員"""

    def __init__(self, name, working_hour=0):
        self.working_hour = working_hour
        super().__init__(name)

    def get_salary(self):
        return 200.0 * self.working_hour


class Salesman(Employee):
    """銷售員"""

    def __init__(self, name, sales=0.0):
        self.sales = sales
        super().__init__(name)

    def get_salary(self):
        return 1800.0 + self.sales * 0.05


class EmployeeFactory():
    """創建員工的工廠（工廠模式 - 通過工廠實現對象使用者和對象之間的解耦合）"""

    @staticmethod
    def create(emp_type, *args, **kwargs):
        """創建員工"""
        emp_type = emp_type.upper()
        emp = None
        if emp_type == 'M':
            emp = Manager(*args, **kwargs)
        elif emp_type == 'P':
            emp = Programmer(*args, **kwargs)
        elif emp_type == 'S':
            emp = Salesman(*args, **kwargs)
        return emp
