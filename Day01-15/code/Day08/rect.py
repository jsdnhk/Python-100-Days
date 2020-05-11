"""
定義和使用矩形類

Version: 0.1
Author: 駱昊
Date: 2018-03-08
"""


class Rect(object):
    """矩形類"""

    def __init__(self, width=0, height=0):
        """初始化方法"""
        self.__width = width
        self.__height = height

    def perimeter(self):
        """計算周長"""
        return (self.__width + self.__height) * 2

    def area(self):
        """計算面積"""
        return self.__width * self.__height

    def __str__(self):
        """矩形對象的字符串表達式"""
        return '矩形[%f,%f]' % (self.__width, self.__height)

    def __del__(self):
        """析構器"""
        print('銷燬矩形對象')


if __name__ == '__main__':
    rect1 = Rect()
    print(rect1)
    print(rect1.perimeter())
    print(rect1.area())
    rect2 = Rect(3.5, 4.5)
    print(rect2)
    print(rect2.perimeter())
    print(rect2.area())
