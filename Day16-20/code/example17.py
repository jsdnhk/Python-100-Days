"""
多重繼承 - 一個類有兩個或者兩個以上的父類
MRO - 方法解析順序 - Method Resolution Order
當出現菱形繼承（鑽石繼承）的時候，子類到底繼承哪個父類的方法
Python 2.x - 深度優先搜索
Python 3.x - C3算法 - 類似於廣度優先搜索
"""
class A():

    def say_hello(self):
        print('Hello, A')


class B(A):
    pass


class C(A):

    def say_hello(self):
        print('Hello, C')


class D(B, C):
    pass


class SetOnceMappingMixin():
    """自定義混入類"""
    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + ' already set')
        return super().__setitem__(key, value)


class SetOnceDict(SetOnceMappingMixin, dict):
    """自定義字典"""
    pass


def main():
    print(D.mro())
    # print(D.__mro__)
    D().say_hello()
    print(SetOnceDict.__mro__)
    my_dict= SetOnceDict()
    my_dict['username'] = 'jackfrued'
    my_dict['username'] = 'hellokitty'


if __name__ == '__main__':
    main()
