"""
變量的作用域以及Python搜索變量的順序
LEGB: Local --> Embedded --> Global --> Built-in
global - 聲明或定義全局變量（要麼直接使用現有的全局作用域的變量，要麼定義一個變量放到全局作用域）
nonlocal - 聲明使用嵌套作用域的變量（如果嵌套作用域沒有對應的變量直接報錯）
"""
x = 100


def foo():
    global x
    x = 200

    def bar():
        x = 300
        print(x)

    bar()
    print(x)


foo()
print(x)
