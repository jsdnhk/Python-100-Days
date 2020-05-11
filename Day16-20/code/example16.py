"""
魔術方法
如果要把自定義對象放到set或者用作dict的鍵
那麼必須要重寫__hash__和__eq__兩個魔術方法
前者用來計算對象的哈希碼，後者用來判斷兩個對象是否相同
哈希碼不同的對象一定是不同的對象，但哈希碼相同未必是相同的對象（哈希碼衝撞）
所以在哈希碼相同的時候還要通過__eq__來判定對象是否相同
"""


class Student():
    __slots__ = ('stuid', 'name', 'gender')

    def __init__(self, stuid, name):
        self.stuid = stuid
        self.name = name

    def __hash__(self):
        return hash(self.stuid) + hash(self.name)

    def __eq__(self, other):
        return self.stuid == other.stuid and \
            self.name == other.name

    def __str__(self):
        return f'{self.stuid}: {self.name}'

    def __repr__(self):
        return self.__str__()


class School():

    def __init__(self, name):
        self.name = name
        self.students = {}

    def __setitem__(self, key, student):
        self.students[key] = student

    def __getitem__(self, key):
        return self.students[key]


def main():
    # students = set()
    # students.add(Student(1001, '王大錘'))
    # students.add(Student(1001, '王大錘'))
    # students.add(Student(1001, '白元芳'))
    # print(len(students))
    # print(students)
    stu = Student(1234, '駱昊')
    stu.gender = 'Male'
    # stu.birth = '1980-11-28'
    print(stu.name, stu.birth)
    school = School('千鋒教育')
    school[1001] = Student(1001, '王大錘')
    school[1002] = Student(1002, '白元芳')
    school[1003] = Student(1003, '白潔')
    print(school[1002])
    print(school[1003])


if __name__ == '__main__':
    main()

