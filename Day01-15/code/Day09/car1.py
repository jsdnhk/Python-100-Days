"""
屬性的使用
- 訪問器/修改器/刪除器
- 使用__slots__對屬性加以限制

Version: 0.1
Author: 駱昊
Date: 2018-03-12
"""


class Car(object):

    __slots__ = ('_brand', '_max_speed')

    def __init__(self, brand, max_speed):
        self._brand = brand
        self._max_speed = max_speed

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @brand.deleter
    def brand(self):
        del self._brand

    @property
    def max_speed(self):
        return self._max_speed

    @max_speed.setter
    def max_speed(self, max_speed):
        if max_speed < 0:
            raise ValueError('Invalid max speed for car')
        self._max_speed = max_speed

    def __str__(self):
        return 'Car: [品牌=%s, 最高時速=%d]' % (self._brand, self._max_speed)


car = Car('QQ', 120)
print(car)
# ValueError
# car.max_speed = -100
car.max_speed = 320
car.brand = "Benz"
# 使用__slots__屬性限制後下面的代碼將產生異常
# car.current_speed = 80
print(car)
# 如果提供了刪除器可以執行下面的代碼
# del car.brand
# 屬性的實現
print(Car.brand)
print(Car.brand.fget)
print(Car.brand.fset)
print(Car.brand.fdel)
# 通過上面的代碼幫助學生理解之前提到的包裝器的概念
# Python中有很多類似的語法糖後面還會出現這樣的東西
