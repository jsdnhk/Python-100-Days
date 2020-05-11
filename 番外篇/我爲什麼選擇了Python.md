## 我爲什麼選擇了Python

目前，Python語言的發展勢頭在國內國外都是不可阻擋的，Python憑藉其簡單優雅的語法，強大的生態圈從衆多語言中脫穎而出，如今已經是穩坐編程語言排行榜前三的位置。國內很多Python開發者都是從Java開發者跨界過來的，我自己也不例外。我簡單的跟大家交代一下，我爲什麼選擇了Python。

### Python vs. Java

我們通過幾個例子來比較一下，做同樣的事情Java和Python的代碼都是怎麼寫的。

例子1：在終端中輸出“hello, world”。

Java代碼：

```Java
class Test {
	
    public static void main(String[] args) {
        System.out.println("hello, world");
    }
}
```

Python代碼：

```Python
print('hello, world')
```

例子2：從1到100求和。

Java代碼：

```Java
class Test {
    
    public static void main(String[] args) {
        int total = 0;
        for (int i = 1; i <= 100; i += 1) {
            total += i;
        }
        System.out.println(total);
    }
}
```

Python代碼：

```Python
print(sum(range(1, 101)))
```

例子3：雙色球隨機選號。

Java代碼：

```Java
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

class Test {

    /**
     * 產生[min, max)範圍的隨機整數
     */
    public static int randomInt(int min, int max) {
        return (int) (Math.random() * (max - min) + min);
    }

    public static void main(String[] args) {
        // 初始化備選紅色球
        List<Integer> redBalls = new ArrayList<>();
        for (int i = 1; i <= 33; ++i) {
            redBalls.add(i);
        }
        List<Integer> selectedBalls = new ArrayList<>();
        // 選出六個紅色球
        for (int i = 0; i < 6; ++i) {
            selectedBalls.add(redBalls.remove(randomInt(0, redBalls.size())));
        }
        // 對紅色球進行排序
        Collections.sort(selectedBalls);
        // 添加一個藍色球
        selectedBalls.add(randomInt(1, 17));
        // 輸出選中的隨機號碼
        for (int i = 0; i < selectedBalls.size(); ++i) {
            System.out.printf("%02d ", selectedBalls.get(i));
            if (i == selectedBalls.size() - 2) {
                System.out.print("| ");
            }
        }
        System.out.println();
    }
}
```

Python代碼：

```Python
from random import randint, sample

# 初始化備選紅色球
red_balls = [x for x in range(1, 34)]
# 選出六個紅色球
selected_balls = sample(red_balls, 6)
# 對紅色球進行排序
selected_balls.sort()
# 添加一個藍色球
selected_balls.append(randint(1, 16))
# 輸出選中的隨機號碼
for index, ball in enumerate(selected_balls):
    print('%02d' % ball, end=' ')
    if index == len(selected_balls) - 2:
        print('|', end=' ')
print()
```

相信，看完這些例子後，你一定感受到了我選擇了Python是有道理的。