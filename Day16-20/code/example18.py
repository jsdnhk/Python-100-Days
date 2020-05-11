"""
元 - meta
元數據 - 描述數據的數據 - metadata
元類 - 描述類的類 - metaclass - 繼承自type
"""
import threading


class SingletonMeta(type):
    """自定義元類"""

    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        cls.lock = threading.Lock()
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            with cls.lock:
                if cls.__instance is None:
                    cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class President(metaclass=SingletonMeta):
    """總統(單例類)"""

    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __str__(self):
        return f'{self.country}: {self.name}'


def main():
    """主函數"""
    p1 = President('特朗普', '美國')
    p2 = President('奧巴馬', '美國')
    p3 = President.__call__('克林頓', '美國')
    print(p1 == p2)
    print(p1 == p3)
    print(p1, p2, p3, sep='\n')


if __name__ == '__main__':
    main()
