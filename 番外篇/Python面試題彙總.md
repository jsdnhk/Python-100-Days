# Python面試題彙總

> 說明：下面的內容源於GitHub上名爲[interview_python](https://github.com/taizilongxu/interview_python)的項目，對其內容進行了修訂和補充。

[TOC]

## Python語言特性

### 1 Python的函數參數傳遞

看兩個例子:

```python
a = 1
def fun(a):
    a = 2
fun(a)
print a  # 1
```

```python
a = []
def fun(a):
    a.append(1)
fun(a)
print a  # [1]
```

所有的變量都可以理解是內存中一個對象的“引用”，或者，也可以看似c中void*的感覺。

通過`id`來看引用`a`的內存地址可以比較理解：

```python
a = 1
def fun(a):
    print "func_in",id(a)   # func_in 41322472
    a = 2
    print "re-point",id(a), id(2)   # re-point 41322448 41322448
print "func_out",id(a), id(1)  # func_out 41322472 41322472
fun(a)
print a  # 1
```

注：具體的值在不同電腦上運行時可能不同。

可以看到，在執行完`a = 2`之後，`a`引用中保存的值，即內存地址發生變化，由原來`1`對象的所在的地址變成了`2`這個實體對象的內存地址。

而第2個例子`a`引用保存的內存值就不會發生變化：

```python
a = []
def fun(a):
    print "func_in",id(a)  # func_in 53629256
    a.append(1)
print "func_out",id(a)     # func_out 53629256
fun(a)
print a  # [1]
```

這裏記住的是類型是屬於對象的，而不是變量。而對象有兩種,“可更改”（mutable）與“不可更改”（immutable）對象。在python中，strings, tuples, 和numbers是不可更改的對象，而 list, dict, set 等則是可以修改的對象。(這就是這個問題的重點)

當一個引用傳遞給函數的時候,函數自動複製一份引用,這個函數裏的引用和外邊的引用沒有半毛關係了.所以第一個例子裏函數把引用指向了一個不可變對象,當函數返回的時候,外面的引用沒半毛感覺.而第二個例子就不一樣了,函數內的引用指向的是可變對象,對它的操作就和定位了指針地址一樣,在內存裏進行修改.

如果還不明白的話,這裏有更好的解釋: http://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference

### 2 Python中的元類(metaclass)

這個非常的不常用,但是像ORM這種複雜的結構還是會需要的,詳情請看:http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python

### 3 @staticmethod和@classmethod

Python其實有3個方法,即靜態方法(staticmethod),類方法(classmethod)和實例方法,如下:

```python
def foo(x):
    print "executing foo(%s)"%(x)

class A(object):
    def foo(self,x):
        print "executing foo(%s,%s)"%(self,x)

    @classmethod
    def class_foo(cls,x):
        print "executing class_foo(%s,%s)"%(cls,x)

    @staticmethod
    def static_foo(x):
        print "executing static_foo(%s)"%x

a=A()

```

這裏先理解下函數參數裏面的self和cls.這個self和cls是對類或者實例的綁定,對於一般的函數來說我們可以這麼調用`foo(x)`,這個函數就是最常用的,它的工作跟任何東西(類,實例)無關.對於實例方法,我們知道在類裏每次定義方法的時候都需要綁定這個實例,就是`foo(self, x)`,爲什麼要這麼做呢?因爲實例方法的調用離不開實例,我們需要把實例自己傳給函數,調用的時候是這樣的`a.foo(x)`(其實是`foo(a, x)`).類方法一樣,只不過它傳遞的是類而不是實例,`A.class_foo(x)`.注意這裏的self和cls可以替換別的參數,但是python的約定是這倆,還是不要改的好.

對於靜態方法其實和普通的方法一樣,不需要對誰進行綁定,唯一的區別是調用的時候需要使用`a.static_foo(x)`或者`A.static_foo(x)`來調用.

| \\      | 實例方法     | 類方法            | 靜態方法            |
| :------ | :------- | :------------- | :-------------- |
| a = A() | a.foo(x) | a.class_foo(x) | a.static_foo(x) |
| A       | 不可用      | A.class_foo(x) | A.static_foo(x) |

更多關於這個問題:
1. http://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod-in-python
2. https://realpython.com/blog/python/instance-class-and-static-methods-demystified/
### 4 類變量和實例變量

**類變量：**

> 	是可在類的所有實例之間共享的值（也就是說，它們不是單獨分配給每個實例的）。例如下例中，num_of_instance 就是類變量，用於跟蹤存在着多少個Test 的實例。

**實例變量：**

> 實例化之後，每個實例單獨擁有的變量。

```python
class Test(object):  
    num_of_instance = 0  
    def __init__(self, name):  
        self.name = name  
        Test.num_of_instance += 1  
  
if __name__ == '__main__':  
    print Test.num_of_instance   # 0
    t1 = Test('jack')  
    print Test.num_of_instance   # 1
    t2 = Test('lucy')  
    print t1.name , t1.num_of_instance  # jack 2
    print t2.name , t2.num_of_instance  # lucy 2
```

> 補充的例子

```python
class Person:
    name="aaa"

p1=Person()
p2=Person()
p1.name="bbb"
print p1.name  # bbb
print p2.name  # aaa
print Person.name  # aaa
```

這裏`p1.name="bbb"`是實例調用了類變量,這其實和上面第一個問題一樣,就是函數傳參的問題,`p1.name`一開始是指向的類變量`name="aaa"`,但是在實例的作用域裏把類變量的引用改變了,就變成了一個實例變量,self.name不再引用Person的類變量name了.

可以看看下面的例子:

```python
class Person:
    name=[]

p1=Person()
p2=Person()
p1.name.append(1)
print p1.name  # [1]
print p2.name  # [1]
print Person.name  # [1]
```

參考:http://stackoverflow.com/questions/6470428/catch-multiple-exceptions-in-one-line-except-block

### 5 Python自省

這個也是python彪悍的特性.

自省就是面向對象的語言所寫的程序在運行時,所能知道對象的類型.簡單一句就是運行時能夠獲得對象的類型.比如type(),dir(),getattr(),hasattr(),isinstance().

```python
a = [1,2,3]
b = {'a':1,'b':2,'c':3}
c = True
print type(a),type(b),type(c) # <type 'list'> <type 'dict'> <type 'bool'>
print isinstance(a,list)  # True
```



### 6 字典推導式

可能你見過列表推導時,卻沒有見過字典推導式,在2.7中才加入的:

```python
d = {key: value for (key, value) in iterable}
```

### 7 Python中單下劃線和雙下劃線

```python
>>> class MyClass():
...     def __init__(self):
...             self.__superprivate = "Hello"
...             self._semiprivate = ", world!"
...
>>> mc = MyClass()
>>> print mc.__superprivate
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: myClass instance has no attribute '__superprivate'
>>> print mc._semiprivate
, world!
>>> print mc.__dict__
{'_MyClass__superprivate': 'Hello', '_semiprivate': ', world!'}
```

`__foo__`:一種約定,Python內部的名字,用來區別其他用戶自定義的命名,以防衝突，就是例如`__init__()`,`__del__()`,`__call__()`這些特殊方法

`_foo`:一種約定,用來指定變量私有.程序員用來指定私有變量的一種方式.不能用from module import * 導入，其他方面和公有一樣訪問；

`__foo`:這個有真正的意義:解析器用`_classname__foo`來代替這個名字,以區別和其他類相同的命名,它無法直接像公有成員一樣隨便訪問,通過對象名._類名__xxx這樣的方式可以訪問.

詳情見:http://stackoverflow.com/questions/1301346/the-meaning-of-a-single-and-a-double-underscore-before-an-object-name-in-python

或者: http://www.zhihu.com/question/19754941

### 8 字符串格式化:%和.format

.format在許多方面看起來更便利.對於`%`最煩人的是它無法同時傳遞一個變量和元組.你可能會想下面的代碼不會有什麼問題:

```
"hi there %s" % name
```

但是,如果name恰好是(1,2,3),它將會拋出一個TypeError異常.爲了保證它總是正確的,你必須這樣做:

```
"hi there %s" % (name,)   # 提供一個單元素的數組而不是一個參數
```

但是有點醜..format就沒有這些問題.你給的第二個問題也是這樣,.format好看多了.

你爲什麼不用它?

* 不知道它(在讀這個之前)
* 爲了和Python2.5兼容(譬如logging庫建議使用`%`([issue #4](https://github.com/taizilongxu/interview_python/issues/4)))

http://stackoverflow.com/questions/5082452/python-string-formatting-vs-format

### 9 迭代器和生成器

這個是stackoverflow裏python排名第一的問題,值得一看: http://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python

這是中文版: http://taizilongxu.gitbooks.io/stackoverflow-about-python/content/1/README.html

這裏有個關於生成器的創建問題面試官有考：
問：  將列表生成式中[]改成() 之後數據結構是否改變？ 
答案：是，從列表變爲生成器

```python
>>> L = [x*x for x in range(10)]
>>> L
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> g = (x*x for x in range(10))
>>> g
<generator object <genexpr> at 0x0000028F8B774200>
```
通過列表生成式，可以直接創建一個列表。但是，受到內存限制，列表容量肯定是有限的。而且，創建一個包含百萬元素的列表，不僅是佔用很大的內存空間，如：我們只需要訪問前面的幾個元素，後面大部分元素所佔的空間都是浪費的。因此，沒有必要創建完整的列表（節省大量內存空間）。在Python中，我們可以採用生成器：邊循環，邊計算的機制—>generator

### 10 `*args` and `**kwargs`

用`*args`和`**kwargs`只是爲了方便並沒有強制使用它們.

當你不確定你的函數裏將要傳遞多少參數時你可以用`*args`.例如,它可以傳遞任意數量的參數:

```python
>>> def print_everything(*args):
        for count, thing in enumerate(args):
...         print '{0}. {1}'.format(count, thing)
...
>>> print_everything('apple', 'banana', 'cabbage')
0. apple
1. banana
2. cabbage
```

相似的,`**kwargs`允許你使用沒有事先定義的參數名:

```python
>>> def table_things(**kwargs):
...     for name, value in kwargs.items():
...         print '{0} = {1}'.format(name, value)
...
>>> table_things(apple = 'fruit', cabbage = 'vegetable')
cabbage = vegetable
apple = fruit
```

你也可以混着用.命名參數首先獲得參數值然後所有的其他參數都傳遞給`*args`和`**kwargs`.命名參數在列表的最前端.例如:

```
def table_things(titlestring, **kwargs)
```

`*args`和`**kwargs`可以同時在函數的定義中,但是`*args`必須在`**kwargs`前面.

當調用函數時你也可以用`*`和`**`語法.例如:

```python
>>> def print_three_things(a, b, c):
...     print 'a = {0}, b = {1}, c = {2}'.format(a,b,c)
...
>>> mylist = ['aardvark', 'baboon', 'cat']
>>> print_three_things(*mylist)

a = aardvark, b = baboon, c = cat
```

就像你看到的一樣,它可以傳遞列表(或者元組)的每一項並把它們解包.注意必須與它們在函數裏的參數相吻合.當然,你也可以在函數定義或者函數調用時用*.

http://stackoverflow.com/questions/3394835/args-and-kwargs

### 11 面向切面編程AOP和裝飾器

這個AOP一聽起來有點懵,同學面阿里的時候就被問懵了...

裝飾器是一個很著名的設計模式，經常被用於有切面需求的場景，較爲經典的有插入日誌、性能測試、事務處理等。裝飾器是解決這類問題的絕佳設計，有了裝飾器，我們就可以抽離出大量函數中與函數功能本身無關的雷同代碼並繼續重用。概括的講，**裝飾器的作用就是爲已經存在的對象添加額外的功能。**

這個問題比較大,推薦: http://stackoverflow.com/questions/739654/how-can-i-make-a-chain-of-function-decorators-in-python

中文: http://taizilongxu.gitbooks.io/stackoverflow-about-python/content/3/README.html

### 12 鴨子類型

“當看到一隻鳥走起來像鴨子、游泳起來像鴨子、叫起來也像鴨子，那麼這隻鳥就可以被稱爲鴨子。”

我們並不關心對象是什麼類型，到底是不是鴨子，只關心行爲。

比如在python中，有很多file-like的東西，比如StringIO,GzipFile,socket。它們有很多相同的方法，我們把它們當作文件使用。

又比如list.extend()方法中,我們並不關心它的參數是不是list,只要它是可迭代的,所以它的參數可以是list/tuple/dict/字符串/生成器等.

鴨子類型在動態語言中經常使用，非常靈活，使得python不想java那樣專門去弄一大堆的設計模式。

### 13 Python中重載

引自知乎:http://www.zhihu.com/question/20053359

函數重載主要是爲了解決兩個問題。

1. 可變參數類型。
2. 可變參數個數。

另外，一個基本的設計原則是，僅僅當兩個函數除了參數類型和參數個數不同以外，其功能是完全相同的，此時才使用函數重載，如果兩個函數的功能其實不同，那麼不應當使用重載，而應當使用一個名字不同的函數。

好吧，那麼對於情況 1 ，函數功能相同，但是參數類型不同，python 如何處理？答案是根本不需要處理，因爲 python 可以接受任何類型的參數，如果函數的功能相同，那麼不同的參數類型在 python 中很可能是相同的代碼，沒有必要做成兩個不同函數。

那麼對於情況 2 ，函數功能相同，但參數個數不同，python 如何處理？大家知道，答案就是缺省參數。對那些缺少的參數設定爲缺省參數即可解決問題。因爲你假設函數功能相同，那麼那些缺少的參數終歸是需要用的。

好了，鑑於情況 1 跟 情況 2 都有了解決方案，python 自然就不需要函數重載了。

### 14 新式類和舊式類

這個面試官問了,我說了老半天,不知道他問的真正意圖是什麼.

[stackoverflow](http://stackoverflow.com/questions/54867/what-is-the-difference-between-old-style-and-new-style-classes-in-python)

這篇文章很好的介紹了新式類的特性: http://www.cnblogs.com/btchenguang/archive/2012/09/17/2689146.html

新式類很早在2.2就出現了,所以舊式類完全是兼容的問題,Python3裏的類全部都是新式類.這裏有一個MRO問題可以瞭解下(新式類是廣度優先,舊式類是深度優先),<Python核心編程>裏講的也很多.

> 一箇舊式類的深度優先的例子

```python
class A():
    def foo1(self):
        print "A"
class B(A):
    def foo2(self):
        pass
class C(A):
    def foo1(self):
        print "C"
class D(B, C):
    pass

d = D()
d.foo1()

# A
```

**按照經典類的查找順序`從左到右深度優先`的規則，在訪問`d.foo1()`的時候,D這個類是沒有的..那麼往上查找,先找到B,裏面沒有,深度優先,訪問A,找到了foo1(),所以這時候調用的是A的foo1()，從而導致C重寫的foo1()被繞過**



### 15 `__new__`和`__init__`的區別

這個`__new__`確實很少見到,先做了解吧.

1. `__new__`是一個靜態方法,而`__init__`是一個實例方法.
2. `__new__`方法會返回一個創建的實例,而`__init__`什麼都不返回.
3. 只有在`__new__`返回一個cls的實例時後面的`__init__`才能被調用.
4. 當創建一個新實例時調用`__new__`,初始化一個實例時用`__init__`.

[stackoverflow](http://stackoverflow.com/questions/674304/pythons-use-of-new-and-init)

ps: `__metaclass__`是創建類時起作用.所以我們可以分別使用`__metaclass__`,`__new__`和`__init__`來分別在類創建,實例創建和實例初始化的時候做一些小手腳.

### 16 單例模式

> 	單例模式是一種常用的軟件設計模式。在它的核心結構中只包含一個被稱爲單例類的特殊類。通過單例模式可以保證系統中一個類只有一個實例而且該實例易於外界訪問，從而方便對實例個數的控制並節約系統資源。如果希望在系統中某個類的對象只能存在一個，單例模式是最好的解決方案。
>
> `__new__()`在`__init__()`之前被調用，用於生成實例對象。利用這個方法和類的屬性的特點可以實現設計模式的單例模式。單例模式是指創建唯一對象，單例模式設計的類只能實例
**這個絕對常考啊.絕對要記住1~2個方法,當時面試官是讓手寫的.**

#### 1 使用`__new__`方法

```python
class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

class MyClass(Singleton):
    a = 1
```

#### 2 共享屬性

創建實例時把所有實例的`__dict__`指向同一個字典,這樣它們具有相同的屬性和方法.

```python

class Borg(object):
    _state = {}
    def __new__(cls, *args, **kw):
        ob = super(Borg, cls).__new__(cls, *args, **kw)
        ob.__dict__ = cls._state
        return ob

class MyClass2(Borg):
    a = 1
```

#### 3 裝飾器版本

```python
def singleton(cls):
    instances = {}
    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return getinstance

@singleton
class MyClass:
  ...
```

#### 4 import方法

作爲python的模塊是天然的單例模式

```python
# mysingleton.py
class My_Singleton(object):
    def foo(self):
        pass

my_singleton = My_Singleton()

# to use
from mysingleton import my_singleton

my_singleton.foo()

```
**[單例模式伯樂在線詳細解釋](http://python.jobbole.com/87294/)**

### 17 Python中的作用域

Python 中，一個變量的作用域總是由在代碼中被賦值的地方所決定的。

當 Python 遇到一個變量的話他會按照這樣的順序進行搜索：

本地作用域（Local）→當前作用域被嵌入的本地作用域（Enclosing locals）→全局/模塊作用域（Global）→內置作用域（Built-in）

### 18 GIL線程全局鎖

線程全局鎖(Global Interpreter Lock),即Python爲了保證線程安全而採取的獨立線程運行的限制,說白了就是一個核只能在同一時間運行一個線程.**對於io密集型任務，python的多線程起到作用，但對於cpu密集型任務，python的多線程幾乎佔不到任何優勢，還有可能因爲爭奪資源而變慢。**

見[Python 最難的問題](http://www.oschina.net/translate/pythons-hardest-problem)

解決辦法就是多進程和下面的協程(協程也只是單CPU,但是能減小切換代價提升性能).

### 19 協程

知乎被問到了,呵呵噠,跪了

簡單點說協程是進程和線程的升級版,進程和線程都面臨着內核態和用戶態的切換問題而耗費許多切換時間,而協程就是用戶自己控制切換的時機,不再需要陷入系統的內核態.

Python裏最常見的yield就是協程的思想!可以查看第九個問題.


### 20 閉包

閉包(closure)是函數式編程的重要的語法結構。閉包也是一種組織代碼的結構，它同樣提高了代碼的可重複使用性。

當一個內嵌函數引用其外部作作用域的變量,我們就會得到一個閉包. 總結一下,創建一個閉包必須滿足以下幾點:

1. 必須有一個內嵌函數
2. 內嵌函數必須引用外部函數中的變量
3. 外部函數的返回值必須是內嵌函數

感覺閉包還是有難度的,幾句話是說不明白的,還是查查相關資料.

重點是函數運行後並不會被撤銷,就像16題的instance字典一樣,當函數運行完後,instance並不被銷燬,而是繼續留在內存空間裏.這個功能類似類裏的類變量,只不過遷移到了函數上.

閉包就像個空心球一樣,你知道外面和裏面,但你不知道中間是什麼樣.

### 21 lambda函數

其實就是一個匿名函數,爲什麼叫lambda?因爲和後面的函數式編程有關.

推薦: [知乎](http://www.zhihu.com/question/20125256)


### 22 Python函數式編程

這個需要適當的瞭解一下吧,畢竟函數式編程在Python中也做了引用.

推薦: [酷殼](http://coolshell.cn/articles/10822.html)

python中函數式編程支持:

filter 函數的功能相當於過濾器。調用一個布爾函數`bool_func`來迭代遍歷每個seq中的元素；返回一個使`bool_seq`返回值爲true的元素的序列。

```python
>>>a = [1,2,3,4,5,6,7]
>>>b = filter(lambda x: x > 5, a)
>>>print b
>>>[6,7]
```

map函數是對一個序列的每個項依次執行函數，下面是對一個序列每個項都乘以2：

```python
>>> a = map(lambda x:x*2,[1,2,3])
>>> list(a)
[2, 4, 6]
```

reduce函數是對一個序列的每個項迭代調用函數，下面是求3的階乘：

```python
>>> reduce(lambda x,y:x*y,range(1,4))
6
```

### 23 Python裏的拷貝

引用和copy(),deepcopy()的區別

```python
import copy
a = [1, 2, 3, 4, ['a', 'b']]  #原始對象

b = a  #賦值，傳對象的引用
c = copy.copy(a)  #對象拷貝，淺拷貝
d = copy.deepcopy(a)  #對象拷貝，深拷貝

a.append(5)  #修改對象a
a[4].append('c')  #修改對象a中的['a', 'b']數組對象

print 'a = ', a
print 'b = ', b
print 'c = ', c
print 'd = ', d

輸出結果：
a =  [1, 2, 3, 4, ['a', 'b', 'c'], 5]
b =  [1, 2, 3, 4, ['a', 'b', 'c'], 5]
c =  [1, 2, 3, 4, ['a', 'b', 'c']]
d =  [1, 2, 3, 4, ['a', 'b']]
```

### 24 Python垃圾回收機制

Python GC主要使用引用計數（reference counting）來跟蹤和回收垃圾。在引用計數的基礎上，通過“標記-清除”（mark and sweep）解決容器對象可能產生的循環引用問題，通過“分代回收”（generation collection）以空間換時間的方法提高垃圾回收效率。

#### 1 引用計數

PyObject是每個對象必有的內容，其中`ob_refcnt`就是做爲引用計數。當一個對象有新的引用時，它的`ob_refcnt`就會增加，當引用它的對象被刪除，它的`ob_refcnt`就會減少.引用計數爲0時，該對象生命就結束了。

優點:

1. 簡單
2. 實時性

缺點:

1. 維護引用計數消耗資源
2. 循環引用

#### 2 標記-清除機制

基本思路是先按需分配，等到沒有空閒內存的時候從寄存器和程序棧上的引用出發，遍歷以對象爲節點、以引用爲邊構成的圖，把所有可以訪問到的對象打上標記，然後清掃一遍內存空間，把所有沒標記的對象釋放。

#### 3 分代技術

分代回收的整體思想是：將系統中的所有內存塊根據其存活時間劃分爲不同的集合，每個集合就成爲一個“代”，垃圾收集頻率隨着“代”的存活時間的增大而減小，存活時間通常利用經過幾次垃圾回收來度量。

Python默認定義了三代對象集合，索引數越大，對象存活時間越長。

舉例：
當某些內存塊M經過了3次垃圾收集的清洗之後還存活時，我們就將內存塊M劃到一個集合A中去，而新分配的內存都劃分到集合B中去。當垃圾收集開始工作時，大多數情況都只對集合B進行垃圾回收，而對集合A進行垃圾回收要隔相當長一段時間後才進行，這就使得垃圾收集機制需要處理的內存少了，效率自然就提高了。在這個過程中，集合B中的某些內存塊由於存活時間長而會被轉移到集合A中，當然，集合A中實際上也存在一些垃圾，這些垃圾的回收會因爲這種分代的機制而被延遲。

### 25 Python的List

推薦: http://www.jianshu.com/p/J4U6rR

### 26 Python的is

is是對比地址,==是對比值

### 27 read,readline和readlines

* read        讀取整個文件
* readline    讀取下一行,使用生成器方法
* readlines   讀取整個文件到一個迭代器以供我們遍歷

### 28 Python2和3的區別
推薦：[Python 2.7.x 與 Python 3.x 的主要差異](http://chenqx.github.io/2014/11/10/Key-differences-between-Python-2-7-x-and-Python-3-x/)

### 29 super init
super() lets you avoid referring to the base class explicitly, which can be nice. But the main advantage comes with multiple inheritance, where all sorts of fun stuff can happen. See the standard docs on super if you haven't already.

Note that the syntax changed in Python 3.0: you can just say super().`__init__`() instead of super(ChildB, self).`__init__`() which IMO is quite a bit nicer.

http://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods

[Python2.7中的super方法淺見](http://blog.csdn.net/mrlevo520/article/details/51712440)

### 30 range and xrange
都在循環時使用，xrange內存性能更好。
for i in range(0, 20):
for i in xrange(0, 20):
What is the difference between range and xrange functions in Python 2.X?
 range creates a list, so if you do range(1, 10000000) it creates a list in memory with 9999999 elements.
 xrange is a sequence object that evaluates lazily.

http://stackoverflow.com/questions/94935/what-is-the-difference-between-range-and-xrange-functions-in-python-2-x

## 操作系統

### 1 select,poll和epoll

其實所有的I/O都是輪詢的方法,只不過實現的層面不同罷了.

這個問題可能有點深入了,但相信能回答出這個問題是對I/O多路複用有很好的瞭解了.其中tornado使用的就是epoll的.

[selec,poll和epoll區別總結](http://www.cnblogs.com/Anker/p/3265058.html)

基本上select有3個缺點:

1. 連接數受限
2. 查找配對速度慢
3. 數據由內核拷貝到用戶態

poll改善了第一個缺點

epoll改了三個缺點.

關於epoll的: http://www.cnblogs.com/my_life/articles/3968782.html

### 2 調度算法

1. 先來先服務(FCFS, First Come First Serve)
2. 短作業優先(SJF, Shortest Job First)
3. 最高優先權調度(Priority Scheduling)
4. 時間片輪轉(RR, Round Robin)
5. 多級反饋隊列調度(multilevel feedback queue scheduling)

常見的調度算法總結:http://www.jianshu.com/p/6edf8174c1eb

實時調度算法:

1. 最早截至時間優先 EDF
2. 最低鬆弛度優先 LLF

### 3 死鎖

原因:
1. 競爭資源
2. 程序推進順序不當

必要條件:
1. 互斥條件
2. 請求和保持條件
3. 不剝奪條件
4. 環路等待條件

處理死鎖基本方法:
1. 預防死鎖(摒棄除1以外的條件)
2. 避免死鎖(銀行家算法)
3. 檢測死鎖(資源分配圖)
4. 解除死鎖
    1. 剝奪資源
    2. 撤銷進程

死鎖概念處理策略詳細介紹:https://wizardforcel.gitbooks.io/wangdaokaoyan-os/content/10.html

### 4 程序編譯與鏈接

推薦: http://www.ruanyifeng.com/blog/2014/11/compiler.html

Bulid過程可以分解爲4個步驟:預處理(Prepressing), 編譯(Compilation)、彙編(Assembly)、鏈接(Linking)

以c語言爲例:

#### 1 預處理

預編譯過程主要處理那些源文件中的以“#”開始的預編譯指令，主要處理規則有：

1. 將所有的“#define”刪除，並展開所用的宏定義
2. 處理所有條件預編譯指令，比如“#if”、“#ifdef”、 “#elif”、“#endif”
3. 處理“#include”預編譯指令，將被包含的文件插入到該編譯指令的位置，注：此過程是遞歸進行的
4. 刪除所有註釋
5. 添加行號和文件名標識，以便於編譯時編譯器產生調試用的行號信息以及用於編譯時產生編譯錯誤或警告時可顯示行號
6. 保留所有的#pragma編譯器指令。

#### 2 編譯

編譯過程就是把預處理完的文件進行一系列的詞法分析、語法分析、語義分析及優化後生成相應的彙編代碼文件。這個過程是整個程序構建的核心部分。

#### 3 彙編

彙編器是將彙編代碼轉化成機器可以執行的指令，每一條彙編語句幾乎都是一條機器指令。經過編譯、鏈接、彙編輸出的文件成爲目標文件(Object File)

#### 4 鏈接

鏈接的主要內容就是把各個模塊之間相互引用的部分處理好，使各個模塊可以正確的拼接。
鏈接的主要過程包塊 地址和空間的分配（Address and Storage Allocation）、符號決議(Symbol Resolution)和重定位(Relocation)等步驟。

### 5 靜態鏈接和動態鏈接

靜態鏈接方法：靜態鏈接的時候，載入代碼就會把程序會用到的動態代碼或動態代碼的地址確定下來
靜態庫的鏈接可以使用靜態鏈接，動態鏈接庫也可以使用這種方法鏈接導入庫

動態鏈接方法：使用這種方式的程序並不在一開始就完成動態鏈接，而是直到真正調用動態庫代碼時，載入程序才計算(被調用的那部分)動態代碼的邏輯地址，然後等到某個時候，程序又需要調用另外某塊動態代碼時，載入程序又去計算這部分代碼的邏輯地址，所以，這種方式使程序初始化時間較短，但運行期間的性能比不上靜態鏈接的程序

### 6 虛擬內存技術

虛擬存儲器是指具有請求調入功能和置換功能,能從邏輯上對內存容量加以擴充的一種存儲系統.

### 7 分頁和分段

分頁: 用戶程序的地址空間被劃分成若干固定大小的區域，稱爲“頁”，相應地，內存空間分成若干個物理塊，頁和塊的大小相等。可將用戶程序的任一頁放在內存的任一塊中，實現了離散分配。

分段: 將用戶程序地址空間分成若干個大小不等的段，每段可以定義一組相對完整的邏輯信息。存儲分配時，以段爲單位，段與段在內存中可以不相鄰接，也實現了離散分配。

#### 分頁與分段的主要區別

1. 頁是信息的物理單位,分頁是爲了實現非連續分配,以便解決內存碎片問題,或者說分頁是由於系統管理的需要.段是信息的邏輯單位,它含有一組意義相對完整的信息,分段的目的是爲了更好地實現共享,滿足用戶的需要.
2. 頁的大小固定,由系統確定,將邏輯地址劃分爲頁號和頁內地址是由機器硬件實現的.而段的長度卻不固定,決定於用戶所編寫的程序,通常由編譯程序在對源程序進行編譯時根據信息的性質來劃分.
3. 分頁的作業地址空間是一維的.分段的地址空間是二維的.

### 8 頁面置換算法

1. 最佳置換算法OPT:不可能實現
2. 先進先出FIFO
3. 最近最久未使用算法LRU:最近一段時間裏最久沒有使用過的頁面予以置換.
4. clock算法

### 9 邊沿觸發和水平觸發

邊緣觸發是指每當狀態變化時發生一個 io 事件，條件觸發是隻要滿足條件就發生一個 io 事件

## 數據庫

### 1 事務

數據庫事務(Database Transaction) ，是指作爲單個邏輯工作單元執行的一系列操作，要麼完全地執行，要麼完全地不執行。
徹底理解數據庫事務: http://www.hollischuang.com/archives/898

### 2 數據庫索引

推薦: http://tech.meituan.com/mysql-index.html

[MySQL索引背後的數據結構及算法原理](http://blog.codinglabs.org/articles/theory-of-mysql-index.html)

聚集索引,非聚集索引,B-Tree,B+Tree,最左前綴原理

### 3 Redis原理

#### Redis是什麼？

1. 是一個完全開源免費的key-value內存數據庫 
2. 通常被認爲是一個數據結構服務器，主要是因爲其有着豐富的數據結構 strings、map、 list、sets、 sorted sets

#### Redis數據庫

> 	通常侷限點來說，Redis也以消息隊列的形式存在，作爲內嵌的List存在，滿足實時的高併發需求。在使用緩存的時候，redis比memcached具有更多的優勢，並且支持更多的數據類型，把redis當作一箇中間存儲系統，用來處理高併發的數據庫操作

- 速度快：使用標準C寫，所有數據都在內存中完成，讀寫速度分別達到10萬/20萬 
- 持久化：對數據的更新採用Copy-on-write技術，可以異步地保存到磁盤上，主要有兩種策略，一是根據時間，更新次數的快照（save 300 10 ）二是基於語句追加方式(Append-only file，aof) 
- 自動操作：對不同數據類型的操作都是自動的，很安全 
- 快速的主--從複製，官方提供了一個數據，Slave在21秒即完成了對Amazon網站10G key set的複製。 
- Sharding技術： 很容易將數據分佈到多個Redis實例中，數據庫的擴展是個永恆的話題，在關係型數據庫中，主要是以添加硬件、以分區爲主要技術形式的縱向擴展解決了很多的應用場景，但隨着web2.0、移動互聯網、雲計算等應用的興起，這種擴展模式已經不太適合了，所以近年來，像採用主從配置、數據庫複製形式的，Sharding這種技術把負載分佈到多個特理節點上去的橫向擴展方式用處越來越多。

#### Redis缺點

- 是數據庫容量受到物理內存的限制,不能用作海量數據的高性能讀寫,因此Redis適合的場景主要侷限在較小數據量的高性能操作和運算上。
- Redis較難支持在線擴容，在集羣容量達到上限時在線擴容會變得很複雜。爲避免這一問題，運維人員在系統上線時必須確保有足夠的空間，這對資源造成了很大的浪費。


### 4 樂觀鎖和悲觀鎖

悲觀鎖：假定會發生併發衝突，屏蔽一切可能違反數據完整性的操作

樂觀鎖：假設不會發生併發衝突，只在提交操作時檢查是否違反數據完整性。

樂觀鎖與悲觀鎖的具體區別: http://www.cnblogs.com/Bob-FD/p/3352216.html

### 5 MVCC

> 	全稱是Multi-Version Concurrent Control，即多版本併發控制，在MVCC協議下，每個讀操作會看到一個一致性的snapshot，並且可以實現非阻塞的讀。MVCC允許數據具有多個版本，這個版本可以是時間戳或者是全局遞增的事務ID，在同一個時間點，不同的事務看到的數據是不同的。

#### [MySQL](http://lib.csdn.net/base/mysql)的innodb引擎是如何實現MVCC的

innodb會爲每一行添加兩個字段，分別表示該行**創建的版本**和**刪除的版本**，填入的是事務的版本號，這個版本號隨着事務的創建不斷遞增。在repeated read的隔離級別（[事務的隔離級別請看這篇文章](http://blog.csdn.net/chosen0ne/article/details/10036775)）下，具體各種數據庫操作的實現：

- select：滿足以下兩個條件innodb會返回該行數據：
  - 該行的創建版本號小於等於當前版本號，用於保證在select操作之前所有的操作已經執行落地。
  - 該行的刪除版本號大於當前版本或者爲空。刪除版本號大於當前版本意味着有一個併發事務將該行刪除了。
- insert：將新插入的行的創建版本號設置爲當前系統的版本號。
- delete：將要刪除的行的刪除版本號設置爲當前系統的版本號。
- update：不執行原地update，而是轉換成insert + delete。將舊行的刪除版本號設置爲當前版本號，並將新行insert同時設置創建版本號爲當前版本號。

其中，寫操作（insert、delete和update）執行時，需要將系統版本號遞增。

	由於舊數據並不真正的刪除，所以必須對這些數據進行清理，innodb會開啓一個後臺線程執行清理工作，具體的規則是將刪除版本號小於當前系統版本的行刪除，這個過程叫做purge。

通過MVCC很好的實現了事務的隔離性，可以達到repeated read級別，要實現serializable還必須加鎖。

>  參考：[MVCC淺析](http://blog.csdn.net/chosen0ne/article/details/18093187)

### 6 MyISAM和InnoDB

MyISAM 適合於一些需要大量查詢的應用，但其對於有大量寫操作並不是很好。甚至你只是需要update一個字段，整個表都會被鎖起來，而別的進程，就算是讀進程都無法操作直到讀操作完成。另外，MyISAM 對於 SELECT COUNT(*) 這類的計算是超快無比的。

InnoDB 的趨勢會是一個非常複雜的存儲引擎，對於一些小的應用，它會比 MyISAM 還慢。他是它支持“行鎖” ，於是在寫操作比較多的時候，會更優秀。並且，他還支持更多的高級應用，比如：事務。

mysql 數據庫引擎: http://www.cnblogs.com/0201zcr/p/5296843.html
MySQL存儲引擎－－MyISAM與InnoDB區別: https://segmentfault.com/a/1190000008227211

## 網絡

### 1 三次握手

1. 客戶端通過向服務器端發送一個SYN來創建一個主動打開，作爲三次握手的一部分。客戶端把這段連接的序號設定爲隨機數 A。
2. 服務器端應當爲一個合法的SYN回送一個SYN/ACK。ACK 的確認碼應爲 A+1，SYN/ACK 包本身又有一個隨機序號 B。
3. 最後，客戶端再發送一個ACK。當服務端受到這個ACK的時候，就完成了三路握手，並進入了連接創建狀態。此時包序號被設定爲收到的確認號 A+1，而響應則爲 B+1。

### 2 四次揮手

_注意: 中斷連接端可以是客戶端，也可以是服務器端. 下面僅以客戶端斷開連接舉例, 反之亦然._

1. 客戶端發送一個數據分段, 其中的 FIN 標記設置爲1. 客戶端進入 FIN-WAIT 狀態. 該狀態下客戶端只接收數據, 不再發送數據.
2. 服務器接收到帶有 FIN = 1 的數據分段, 發送帶有 ACK = 1 的剩餘數據分段, 確認收到客戶端發來的 FIN 信息.
3. 服務器等到所有數據傳輸結束, 向客戶端發送一個帶有 FIN = 1 的數據分段, 並進入 CLOSE-WAIT 狀態, 等待客戶端發來帶有 ACK = 1 的確認報文.
4. 客戶端收到服務器發來帶有 FIN = 1 的報文, 返回 ACK = 1 的報文確認, 爲了防止服務器端未收到需要重發, 進入 TIME-WAIT 狀態. 服務器接收到報文後關閉連接. 客戶端等待 2MSL 後未收到回覆, 則認爲服務器成功關閉, 客戶端關閉連接.

圖解: http://blog.csdn.net/whuslei/article/details/6667471

### 3 ARP協議

地址解析協議(Address Resolution Protocol)，其基本功能爲透過目標設備的IP地址，查詢目標的MAC地址，以保證通信的順利進行。它是IPv4網絡層必不可少的協議，不過在IPv6中已不再適用，並被鄰居發現協議（NDP）所替代。

### 4 urllib和urllib2的區別

這個面試官確實問過,當時答的urllib2可以Post而urllib不可以.

1. urllib提供urlencode方法用來GET查詢字符串的產生，而urllib2沒有。這是爲何urllib常和urllib2一起使用的原因。
2. urllib2可以接受一個Request類的實例來設置URL請求的headers，urllib僅可以接受URL。這意味着，你不可以僞裝你的User Agent字符串等。

### 5 Post和Get
[GET和POST有什麼區別？及爲什麼網上的多數答案都是錯的](http://www.cnblogs.com/nankezhishi/archive/2012/06/09/getandpost.html)
[知乎回答](https://www.zhihu.com/question/31640769?rf=37401322)

get: [RFC 2616 - Hypertext Transfer Protocol -- HTTP/1.1](http://tools.ietf.org/html/rfc2616#section-9.3)
post: [RFC 2616 - Hypertext Transfer Protocol -- HTTP/1.1](http://tools.ietf.org/html/rfc2616#section-9.5)


### 6 Cookie和Session

|      | Cookie                     | Session |
| :--- | :------------------------- | :------ |
| 儲存位置 | 客戶端                        | 服務器端    |
| 目的   | 跟蹤會話，也可以保存用戶偏好設置或者保存用戶名密碼等 | 跟蹤會話    |
| 安全性  | 不安全                        | 安全      |

session技術是要使用到cookie的，之所以出現session技術，主要是爲了安全。

### 7 apache和nginx的區別

nginx 相對 apache 的優點：
* 輕量級，同樣起web 服務，比apache 佔用更少的內存及資源
* 抗併發，nginx 處理請求是異步非阻塞的，支持更多的併發連接，而apache 則是阻塞型的，在高併發下nginx 能保持低資源低消耗高性能
* 配置簡潔
* 高度模塊化的設計，編寫模塊相對簡單
* 社區活躍

apache 相對nginx 的優點：
* rewrite ，比nginx 的rewrite 強大
* 模塊超多，基本想到的都可以找到
* 少bug ，nginx 的bug 相對較多
* 超穩定

### 8 網站用戶密碼保存

1. 明文保存
2. 明文hash後保存,如md5
3. MD5+Salt方式,這個salt可以隨機
4. 知乎使用了Bcrypy(好像)加密

### 9 HTTP和HTTPS


| 狀態碼       | 定義               |
| :-------- | :--------------- |
| 1xx 報告    | 接收到請求，繼續進程       |
| 2xx 成功    | 步驟成功接收，被理解，並被接受  |
| 3xx 重定向   | 爲了完成請求,必須採取進一步措施 |
| 4xx 客戶端出錯 | 請求包括錯的順序或不能完成    |
| 5xx 服務器出錯 | 服務器無法完成顯然有效的請求   |

403: Forbidden
404: Not Found

HTTPS握手,對稱加密,非對稱加密,TLS/SSL,RSA

### 10 XSRF和XSS

* CSRF(Cross-site request forgery)跨站請求僞造
* XSS(Cross Site Scripting)跨站腳本攻擊

CSRF重點在請求,XSS重點在腳本

### 11 冪等 Idempotence

HTTP方法的冪等性是指一次和多次請求某一個資源應該具有同樣的**副作用**。(注意是副作用)

`GET http://www.bank.com/account/123456`，不會改變資源的狀態，不論調用一次還是N次都沒有副作用。請注意，這裏強調的是一次和N次具有相同的副作用，而不是每次GET的結果相同。`GET http://www.news.com/latest-news`這個HTTP請求可能會每次得到不同的結果，但它本身並沒有產生任何副作用，因而是滿足冪等性的。

DELETE方法用於刪除資源，有副作用，但它應該滿足冪等性。比如：`DELETE http://www.forum.com/article/4231`，調用一次和N次對系統產生的副作用是相同的，即刪掉id爲4231的帖子；因此，調用者可以多次調用或刷新頁面而不必擔心引起錯誤。


POST所對應的URI並非創建的資源本身，而是資源的接收者。比如：`POST http://www.forum.com/articles`的語義是在`http://www.forum.com/articles`下創建一篇帖子，HTTP響應中應包含帖子的創建狀態以及帖子的URI。兩次相同的POST請求會在服務器端創建兩份資源，它們具有不同的URI；所以，POST方法不具備冪等性。

PUT所對應的URI是要創建或更新的資源本身。比如：`PUT http://www.forum/articles/4231`的語義是創建或更新ID爲4231的帖子。對同一URI進行多次PUT的副作用和一次PUT是相同的；因此，PUT方法具有冪等性。

### 12 RESTful架構(SOAP,RPC)

推薦: http://www.ruanyifeng.com/blog/2011/09/restful.html

### 13 SOAP

SOAP（原爲Simple Object Access Protocol的首字母縮寫，即簡單對象訪問協議）是交換數據的一種協議規範，使用在計算機網絡Web服務（web service）中，交換帶結構信息。SOAP爲了簡化網頁服務器（Web Server）從XML數據庫中提取數據時，節省去格式化頁面時間，以及不同應用程序之間按照HTTP通信協議，遵從XML格式執行資料互換，使其抽象於語言實現、平臺和硬件。

### 14 RPC

RPC（Remote Procedure Call Protocol）——遠程過程調用協議，它是一種通過網絡從遠程計算機程序上請求服務，而不需要了解底層網絡技術的協議。RPC協議假定某些傳輸協議的存在，如TCP或UDP，爲通信程序之間攜帶信息數據。在OSI網絡通信模型中，RPC跨越了傳輸層和應用層。RPC使得開發包括網絡分佈式多程序在內的應用程序更加容易。

總結:服務提供的兩大流派.傳統意義以方法調用爲導向通稱RPC。爲了企業SOA,若干廠商聯合推出webservice,制定了wsdl接口定義,傳輸soap.當互聯網時代,臃腫SOA被簡化爲http+xml/json.但是簡化出現各種混亂。以資源爲導向,任何操作無非是對資源的增刪改查，於是統一的REST出現了.

進化的順序: RPC -> SOAP -> RESTful

### 15 CGI和WSGI
CGI是通用網關接口，是連接web服務器和應用程序的接口，用戶通過CGI來獲取動態數據或文件等。
CGI程序是一個獨立的程序，它可以用幾乎所有語言來寫，包括perl，c，lua，python等等。

WSGI, Web Server Gateway Interface，是Python應用程序或框架和Web服務器之間的一種接口，WSGI的其中一個目的就是讓用戶可以用統一的語言(Python)編寫前後端。

官方說明：[PEP-3333](https://www.python.org/dev/peps/pep-3333/)

### 16 中間人攻擊

在GFW裏屢見不鮮的,呵呵.

中間人攻擊（Man-in-the-middle attack，通常縮寫爲MITM）是指攻擊者與通訊的兩端分別創建獨立的聯繫，並交換其所收到的數據，使通訊的兩端認爲他們正在通過一個私密的連接與對方直接對話，但事實上整個會話都被攻擊者完全控制。

### 17 c10k問題

所謂c10k問題，指的是服務器同時支持成千上萬個客戶端的問題，也就是concurrent 10 000 connection（這也是c10k這個名字的由來）。
推薦: https://my.oschina.net/xianggao/blog/664275

### 18 socket

推薦: http://www.360doc.com/content/11/0609/15/5482098_122692444.shtml

Socket=Ip address+ TCP/UDP + port

### 19 瀏覽器緩存

推薦: http://www.cnblogs.com/skynet/archive/2012/11/28/2792503.html

304 Not Modified

### 20 HTTP1.0和HTTP1.1

推薦: http://blog.csdn.net/elifefly/article/details/3964766

1. 請求頭Host字段,一個服務器多個網站
2. 長鏈接
3. 文件斷點續傳
4. 身份認證,狀態管理,Cache緩存

HTTP請求8種方法介紹 
HTTP/1.1協議中共定義了8種HTTP請求方法，HTTP請求方法也被叫做“請求動作”，不同的方法規定了不同的操作指定的資源方式。服務端也會根據不同的請求方法做不同的響應。

GET

GET請求會顯示請求指定的資源。一般來說GET方法應該只用於數據的讀取，而不應當用於會產生副作用的非冪等的操作中。

GET會方法請求指定的頁面信息，並返回響應主體，GET被認爲是不安全的方法，因爲GET方法會被網絡蜘蛛等任意的訪問。

HEAD

HEAD方法與GET方法一樣，都是向服務器發出指定資源的請求。但是，服務器在響應HEAD請求時不會回傳資源的內容部分，即：響應主體。這樣，我們可以不傳輸全部內容的情況下，就可以獲取服務器的響應頭信息。HEAD方法常被用於客戶端查看服務器的性能。

POST

POST請求會 向指定資源提交數據，請求服務器進行處理，如：表單數據提交、文件上傳等，請求數據會被包含在請求體中。POST方法是非冪等的方法，因爲這個請求可能會創建新的資源或/和修改現有資源。

PUT

PUT請求會身向指定資源位置上傳其最新內容，PUT方法是冪等的方法。通過該方法客戶端可以將指定資源的最新數據傳送給服務器取代指定的資源的內容。

DELETE

DELETE請求用於請求服務器刪除所請求URI（統一資源標識符，Uniform Resource Identifier）所標識的資源。DELETE請求後指定資源會被刪除，DELETE方法也是冪等的。

CONNECT

CONNECT方法是HTTP/1.1協議預留的，能夠將連接改爲管道方式的代理服務器。通常用於SSL加密服務器的鏈接與非加密的HTTP代理服務器的通信。

OPTIONS

OPTIONS請求與HEAD類似，一般也是用於客戶端查看服務器的性能。 這個方法會請求服務器返回該資源所支持的所有HTTP請求方法，該方法會用’*’來代替資源名稱，向服務器發送OPTIONS請求，可以測試服務器功能是否正常。JavaScript的XMLHttpRequest對象進行CORS跨域資源共享時，就是使用OPTIONS方法發送嗅探請求，以判斷是否有對指定資源的訪問權限。 允許

TRACE

TRACE請求服務器回顯其收到的請求信息，該方法主要用於HTTP請求的測試或診斷。

HTTP/1.1之後增加的方法

在HTTP/1.1標準制定之後，又陸續擴展了一些方法。其中使用中較多的是 PATCH 方法：

PATCH

PATCH方法出現的較晚，它在2010年的RFC 5789標準中被定義。PATCH請求與PUT請求類似，同樣用於資源的更新。二者有以下兩點不同：

但PATCH一般用於資源的部分更新，而PUT一般用於資源的整體更新。 
當資源不存在時，PATCH會創建一個新的資源，而PUT只會對已在資源進行更新。

### 21 Ajax
AJAX,Asynchronous JavaScript and XML（異步的 JavaScript 和 XML）, 是與在不重新加載整個頁面的情況下，與服務器交換數據並更新部分網頁的技術。

## *NIX

### unix進程間通信方式(IPC)

1. 管道（Pipe）：管道可用於具有親緣關係進程間的通信，允許一個進程和另一個與它有共同祖先的進程之間進行通信。
2. 命名管道（named pipe）：命名管道克服了管道沒有名字的限制，因此，除具有管道所具有的功能外，它還允許無親緣關係進程間的通信。命名管道在文件系統中有對應的文件名。命名管道通過命令mkfifo或系統調用mkfifo來創建。
3. 信號（Signal）：信號是比較複雜的通信方式，用於通知接受進程有某種事件發生，除了用於進程間通信外，進程還可以發送信號給進程本身；linux除了支持Unix早期信號語義函數sigal外，還支持語義符合Posix.1標準的信號函數sigaction（實際上，該函數是基於BSD的，BSD爲了實現可靠信號機制，又能夠統一對外接口，用sigaction函數重新實現了signal函數）。
4. 消息（Message）隊列：消息隊列是消息的鏈接表，包括Posix消息隊列system V消息隊列。有足夠權限的進程可以向隊列中添加消息，被賦予讀權限的進程則可以讀走隊列中的消息。消息隊列克服了信號承載信息量少，管道只能承載無格式字節流以及緩衝區大小受限等缺
5. 共享內存：使得多個進程可以訪問同一塊內存空間，是最快的可用IPC形式。是針對其他通信機制運行效率較低而設計的。往往與其它通信機制，如信號量結合使用，來達到進程間的同步及互斥。
6. 內存映射（mapped memory）：內存映射允許任何多個進程間通信，每一個使用該機制的進程通過把一個共享的文件映射到自己的進程地址空間來實現它。
7. 信號量（semaphore）：主要作爲進程間以及同一進程不同線程之間的同步手段。
8. 套接口（Socket）：更爲一般的進程間通信機制，可用於不同機器之間的進程間通信。起初是由Unix系統的BSD分支開發出來的，但現在一般可以移植到其它類Unix系統上：Linux和System V的變種都支持套接字。


## 數據結構

### 1 紅黑樹

紅黑樹與AVL的比較：

AVL是嚴格平衡樹，因此在增加或者刪除節點的時候，根據不同情況，旋轉的次數比紅黑樹要多；

紅黑是用非嚴格的平衡來換取增刪節點時候旋轉次數的降低；

所以簡單說，如果你的應用中，搜索的次數遠遠大於插入和刪除，那麼選擇AVL，如果搜索，插入刪除次數幾乎差不多，應該選擇RB。

紅黑樹詳解: https://xieguanglei.github.io/blog/post/red-black-tree.html

教你透徹瞭解紅黑樹: https://github.com/julycoding/The-Art-Of-Programming-By-July/blob/master/ebook/zh/03.01.md

## 編程題

### 1 臺階問題/斐波那契

一隻青蛙一次可以跳上1級臺階，也可以跳上2級。求該青蛙跳上一個n級的臺階總共有多少種跳法。

```python
fib = lambda n: n if n <= 2 else fib(n - 1) + fib(n - 2)
```

第二種記憶方法

```python
def memo(func):
    cache = {}
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap


@memo
def fib(i):
    if i < 2:
        return 1
    return fib(i-1) + fib(i-2)
```

第三種方法

```python
def fib(n):
    a, b = 0, 1
    for _ in xrange(n):
        a, b = b, a + b
    return b
```

### 2 變態臺階問題

一隻青蛙一次可以跳上1級臺階，也可以跳上2級……它也可以跳上n級。求該青蛙跳上一個n級的臺階總共有多少種跳法。

```python
fib = lambda n: n if n < 2 else 2 * fib(n - 1)
```

### 3 矩形覆蓋

我們可以用`2*1`的小矩形橫着或者豎着去覆蓋更大的矩形。請問用n個`2*1`的小矩形無重疊地覆蓋一個`2*n`的大矩形，總共有多少種方法？

>第`2*n`個矩形的覆蓋方法等於第`2*(n-1)`加上第`2*(n-2)`的方法。

```python
f = lambda n: 1 if n < 2 else f(n - 1) + f(n - 2)
```

### 4 楊氏矩陣查找

在一個m行n列二維數組中，每一行都按照從左到右遞增的順序排序，每一列都按照從上到下遞增的順序排序。請完成一個函數，輸入這樣的一個二維數組和一個整數，判斷數組中是否含有該整數。

使用Step-wise線性搜索。

```python
def get_value(l, r, c):
    return l[r][c]

def find(l, x):
    m = len(l) - 1
    n = len(l[0]) - 1
    r = 0
    c = n
    while c >= 0 and r <= m:
        value = get_value(l, r, c)
        if value == x:
            return True
        elif value > x:
            c = c - 1
        elif value < x:
            r = r + 1
    return False
```

### 5 去除列表中的重複元素

用集合

```python
list(set(l))
```

用字典

```python
l1 = ['b','c','d','b','c','a','a']
l2 = {}.fromkeys(l1).keys()
print l2
```

用字典並保持順序

```python
l1 = ['b','c','d','b','c','a','a']
l2 = list(set(l1))
l2.sort(key=l1.index)
print l2
```

列表推導式

```python
l1 = ['b','c','d','b','c','a','a']
l2 = []
[l2.append(i) for i in l1 if not i in l2]
```

sorted排序並且用列表推導式.

l = ['b','c','d','b','c','a','a']
[single.append(i) for i in sorted(l) if i not in single]
print single

### 6 鏈表成對調換

`1->2->3->4`轉換成`2->1->4->3`.

```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head != None and head.next != None:
            next = head.next
            head.next = self.swapPairs(next.next)
            next.next = head
            return next
        return head
```

### 7 創建字典的方法

#### 1 直接創建

```python
dict = {'name':'earth', 'port':'80'}
```

#### 2 工廠方法

```python
items=[('name','earth'),('port','80')]
dict2=dict(items)
dict1=dict((['name','earth'],['port','80']))
```

#### 3 fromkeys()方法

```python
dict1={}.fromkeys(('x','y'),-1)
dict={'x':-1,'y':-1}
dict2={}.fromkeys(('x','y'))
dict2={'x':None, 'y':None}
```

### 8 合併兩個有序列表

知乎遠程面試要求編程

>  尾遞歸

```python
def _recursion_merge_sort2(l1, l2, tmp):
    if len(l1) == 0 or len(l2) == 0:
        tmp.extend(l1)
        tmp.extend(l2)
        return tmp
    else:
        if l1[0] < l2[0]:
            tmp.append(l1[0])
            del l1[0]
        else:
            tmp.append(l2[0])
            del l2[0]
        return _recursion_merge_sort2(l1, l2, tmp)

def recursion_merge_sort2(l1, l2):
    return _recursion_merge_sort2(l1, l2, [])
```

>  循環算法

思路：

定義一個新的空列表

比較兩個列表的首個元素

小的就插入到新列表裏

把已經插入新列表的元素從舊列表刪除

直到兩個舊列表有一個爲空

再把舊列表加到新列表後面


```pyhton
def loop_merge_sort(l1, l2):
    tmp = []
    while len(l1) > 0 and len(l2) > 0:
        if l1[0] < l2[0]:
            tmp.append(l1[0])
            del l1[0]
        else:
            tmp.append(l2[0])
            del l2[0]
    tmp.extend(l1)
    tmp.extend(l2)
    return tmp
```


> pop彈出

```Python
a = [1,2,3,7]
b = [3,4,5]

def merge_sortedlist(a,b):
    c = []
    while a and b:
        if a[0] >= b[0]:
            c.append(b.pop(0))
        else:
            c.append(a.pop(0))
    while a:
        c.append(a.pop(0))
    while b:
        c.append(b.pop(0))
    return c
print merge_sortedlist(a,b)
    
```


### 9 交叉鏈表求交點

> 其實思想可以按照從尾開始比較兩個鏈表，如果相交，則從尾開始必然一致，只要從尾開始比較，直至不一致的地方即爲交叉點，如圖所示

![](http://hi.csdn.net/attachment/201106/28/0_1309244136MWLP.gif)

```python
# 使用a,b兩個list來模擬鏈表，可以看出交叉點是 7這個節點
a = [1,2,3,7,9,1,5]
b = [4,5,7,9,1,5]

for i in range(1,min(len(a),len(b))):
    if i==1 and (a[-1] != b[-1]):
        print "No"
        break
    else:
        if a[-i] != b[-i]:
            print "交叉節點：",a[-i+1]
            break
        else:
            pass
```

> 另外一種比較正規的方法，構造鏈表類

```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def node(l1, l2):
    length1, lenth2 = 0, 0
    # 求兩個鏈表長度
    while l1.next:
        l1 = l1.next
        length1 += 1
    while l2.next:
        l2 = l2.next
        length2 += 1
    # 長的鏈表先走
    if length1 > lenth2:
        for _ in range(length1 - length2):
            l1 = l1.next
    else:
        for _ in range(length2 - length1):
            l2 = l2.next
    while l1 and l2:
        if l1.next == l2.next:
            return l1.next
        else:
            l1 = l1.next
            l2 = l2.next
```

修改了一下:


```python
#coding:utf-8
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def node(l1, l2):
    length1, length2 = 0, 0
    # 求兩個鏈表長度
    while l1.next:
        l1 = l1.next#尾節點
        length1 += 1
    while l2.next:
        l2 = l2.next#尾節點
        length2 += 1

    #如果相交
    if l1.next == l2.next:
        # 長的鏈表先走
        if length1 > length2:
            for _ in range(length1 - length2):
                l1 = l1.next
            return l1#返回交點
        else:
            for _ in range(length2 - length1):
                l2 = l2.next
            return l2#返回交點
    # 如果不相交
    else:
        return
```


思路: http://humaoli.blog.163.com/blog/static/13346651820141125102125995/


### 10 二分查找


```python

#coding:utf-8
def binary_search(list,item):
    low = 0
    high = len(list)-1
    while low<=high:
        mid = (low+high)/2
        guess = list[mid]
        if guess>item:
            high = mid-1
        elif guess<item:
            low = mid+1
        else:
            return mid
    return None
mylist = [1,3,5,7,9]
print binary_search(mylist,3)

```

參考: http://blog.csdn.net/u013205877/article/details/76411718

### 11 快排

```python
#coding:utf-8
def quicksort(list):
    if len(list)<2:
        return list
    else:
        midpivot = list[0]
        lessbeforemidpivot = [i for i in list[1:] if i<=midpivot]
        biggerafterpivot = [i for i in list[1:] if i > midpivot]
        finallylist = quicksort(lessbeforemidpivot)+[midpivot]+quicksort(biggerafterpivot)
        return finallylist

print quicksort([2,4,6,7,1,2,5])
```


>  更多排序問題可見：[數據結構與算法-排序篇-Python描述](http://blog.csdn.net/mrlevo520/article/details/77829204)


### 12 找零問題


```python

#coding:utf-8
#values是硬幣的面值values = [ 25, 21, 10, 5, 1]
#valuesCounts   錢幣對應的種類數
#money  找出來的總錢數
#coinsUsed   對應於目前錢幣總數i所使用的硬幣數目

def coinChange(values,valuesCounts,money,coinsUsed):
    #遍歷出從1到money所有的錢數可能
    for cents in range(1,money+1):
        minCoins = cents
        #把所有的硬幣面值遍歷出來和錢數做對比
        for kind in range(0,valuesCounts):
            if (values[kind] <= cents):
                temp = coinsUsed[cents - values[kind]] +1
                if (temp < minCoins):
                    minCoins = temp
        coinsUsed[cents] = minCoins
        print ('面值:{0}的最少硬幣使用數爲:{1}'.format(cents, coinsUsed[cents]))

```

思路: http://blog.csdn.net/wdxin1322/article/details/9501163

方法: http://www.cnblogs.com/ChenxofHit/archive/2011/03/18/1988431.html

### 13 廣度遍歷和深度遍歷二叉樹

給定一個數組，構建二叉樹，並且按層次打印這個二叉樹


### 14 二叉樹節點

```python

class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))

```

### 15 層次遍歷

```python

def lookup(root):
    row = [root]
    while row:
        print(row)
        row = [kid for item in row for kid in (item.left, item.right) if kid]

```

### 16 深度遍歷

```python

def deep(root):
    if not root:
        return
    print root.data
    deep(root.left)
    deep(root.right)

if __name__ == '__main__':
    lookup(tree)
    deep(tree)
```

### 17 前中後序遍歷

深度遍歷改變順序就OK了

```python

#coding:utf-8
#二叉樹的遍歷
#簡單的二叉樹節點類
class Node(object):
    def __init__(self,value,left,right):
        self.value = value
        self.left = left
        self.right = right

#中序遍歷:遍歷左子樹,訪問當前節點,遍歷右子樹

def mid_travelsal(root):
    if root.left is None:
        mid_travelsal(root.left)
    #訪問當前節點
    print(root.value)
    if root.right is not None:
        mid_travelsal(root.right)

#前序遍歷:訪問當前節點,遍歷左子樹,遍歷右子樹

def pre_travelsal(root):
    print (root.value)
    if root.left is not None:
        pre_travelsal(root.left)
    if root.right is not None:
        pre_travelsal(root.right)

#後續遍歷:遍歷左子樹,遍歷右子樹,訪問當前節點

def post_trvelsal(root):
    if root.left is not None:
        post_trvelsal(root.left)
    if root.right is not None:
        post_trvelsal(root.right)
    print (root.value)

```

### 18 求最大樹深

```python
def maxDepth(root):
        if not root:
            return 0
        return max(maxDepth(root.left), maxDepth(root.right)) + 1
```

### 19 求兩棵樹是否相同

```python
def isSameTree(p, q):
    if p == None and q == None:
        return True
    elif p and q :
        return p.val == q.val and isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
    else :
        return False
```

### 20 前序中序求後序

推薦: http://blog.csdn.net/hinyunsin/article/details/6315502

```python
def rebuild(pre, center):
    if not pre:
        return
    cur = Node(pre[0])
    index = center.index(pre[0])
    cur.left = rebuild(pre[1:index + 1], center[:index])
    cur.right = rebuild(pre[index + 1:], center[index + 1:])
    return cur

def deep(root):
    if not root:
        return
    deep(root.left)
    deep(root.right)
    print root.data
```

### 21 單鏈表逆置

```python
class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

link = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9)))))))))

def rev(link):
    pre = link
    cur = link.next
    pre.next = None
    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return pre

root = rev(link)
while root:
    print root.data
    root = root.next
```

思路: http://blog.csdn.net/feliciafay/article/details/6841115

方法: http://www.xuebuyuan.com/2066385.html?mobile=1

### 22 兩個字符串是否是變位詞

```python
class Anagram:
    """
    @:param s1: The first string
    @:param s2: The second string
    @:return true or false
    """
    def Solution1(s1,s2):
        alist = list(s2)

        pos1 = 0
        stillOK = True

        while pos1 < len(s1) and stillOK:
            pos2 = 0
            found = False
            while pos2 < len(alist) and not found:
                if s1[pos1] == alist[pos2]:
                    found = True
                else:
                    pos2 = pos2 + 1

            if found:
                alist[pos2] = None
            else:
                stillOK = False

            pos1 = pos1 + 1

        return stillOK

    print(Solution1('abcd','dcba'))

    def Solution2(s1,s2):
        alist1 = list(s1)
        alist2 = list(s2)

        alist1.sort()
        alist2.sort()


        pos = 0
        matches = True

        while pos < len(s1) and matches:
            if alist1[pos] == alist2[pos]:
                pos = pos + 1
            else:
                matches = False

        return matches

    print(Solution2('abcde','edcbg'))

    def Solution3(s1,s2):
        c1 = [0]*26
        c2 = [0]*26

        for i in range(len(s1)):
            pos = ord(s1[i])-ord('a')
            c1[pos] = c1[pos] + 1

        for i in range(len(s2)):
            pos = ord(s2[i])-ord('a')
            c2[pos] = c2[pos] + 1

        j = 0
        stillOK = True
        while j<26 and stillOK:
            if c1[j] == c2[j]:
                j = j + 1
            else:
                stillOK = False

        return stillOK

    print(Solution3('apple','pleap'))
```

### 23 動態規劃問題

>  可參考：[動態規劃(DP)的整理-Python描述](http://blog.csdn.net/mrlevo520/article/details/75676160)
