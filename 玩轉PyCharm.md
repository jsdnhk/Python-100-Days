## 玩轉PyCharm

PyCharm是由JetBrains公司開發的提供給Python專業的開發者的一個集成開發環境，它最大的優點是能夠大大提升Python開發者的工作效率，爲開發者集成了很多用起來非常順手的功能，包括代碼調試、高亮語法、代碼跳轉、智能提示、自動補全、單元測試、版本控制等等。此外，PyCharm還提供了對一些高級功能的支持，包括支持基於Django框架的Web開發。

### PyCharm的下載和安裝

可以在[JetBrains公司的官方網站](<https://www.jetbrains.com/>)找到PyCharm的[下載鏈接](https://www.jetbrains.com/pycharm/download/)，有兩個可供下載的版本，一個是社區版（PyCharm CE），一個是專業版（PyCharm Professional）。社區版在Apache許可證下發布，可以免費使用；專業版在專用許可證下發布，需要購買授權後才能使用，但新用戶可以試用30天。很顯然，專業版提供了更爲強大的功能和對企業級開發的各種支持，但是對於初學者來說，社區版已經足夠強大和好用了。安裝PyCharm只需要直接運行下載的安裝程序，然後持續的點擊“Next”（下一步）按鈕就可以啦。下面是我在Windows系統下安裝PyCharm的截圖，安裝完成後點擊“Finish”（結束）按鈕關閉安裝嚮導，然後可以通過雙擊桌面的快捷方式來運行PyCharm。

![](res/pycharm-installation.png)

### 首次使用的設置

第一次使用PyCharm時，會有一個導入設置的嚮導，如果之前沒有使用PyCharm或者沒有保存過設置的就直接選擇“Do not import settings”進入下一步即可，下面是我在macOS系統下第一次使用PyCharm時的截圖。

![](./res/pycharm-import-settings.png)

專業版的PyCharm是需要激活的，**強烈建議大家在條件允許的情況下支付費用來支持優秀的產品**，如果不用做商業用途或者不需要使用PyCharm的高級功能，我們可以暫時選擇試用30天或者使用社區版的PyCharm。如果你是一名學生，希望購買PyCharm來使用，可以看看[教育優惠官方申請指南](https://sales.jetbrains.com/hc/zh-cn/articles/207154369)。如下圖所示，我們需要點擊“Evaluate”按鈕來試用專業版PyCharm。

![](./res/pycharm-activation.png)

接下來是選擇UI主題，可以根據個人喜好進行選擇，深色的主題比較護眼而淺色的主題對比度更好。

![](./res/pycharm-ui-themes.png)

再接下來是創建可以在“終端”或“命令行提示符”中運行PyCharm的啓動腳本，當然也可以不做任何勾選，直接點擊“Next: Featured plugins”按鈕進入下一環節。

![](./res/pycharm-create-launcher.png)

然後可以選擇需要安裝哪些插件，我們可以暫時什麼都不安裝，等需要的時候再來決定。

![](./res/pycharm-install-plugins.png)

最後點擊上圖右下角的“Start using PyCharm”（開始使用PyCharm）就可以開啓你的PyCharm之旅了。

### 用PyCharm創建項目

啓動PyCharm之後會來到一個歡迎頁，在歡迎頁上我們可以選擇“創建新項目”（Create New Project）、“打開已有項目”（Open）和“從版本控制系統中檢出項目”（Get from Version Control）。

![](./res/pycharm-welcome.png)

如果選擇了“Create New Project”來創建新項目就會打一個創建項目的嚮導頁。下圖所示是PyCharm專業版創建新項目的嚮導頁，可以看出專業版支持的項目類型非常的多，而社區版只能創建純Python項目（Pure Python），沒有這一系列的選項。

![](./res/pycharm-project-wizard.png)

接下來，我們要爲項目創建專屬的虛擬環境，每個Python項目最好都在自己專屬的虛擬環境中運行，因爲每個項目對Python解釋器和三方庫的需求並不相同，虛擬環境對不同的項目進行了隔離。在上圖所示的界面在，我們可以選擇新建虛擬環境（New environment using Virtualenv），這裏的“Virtualenv”是PyCharm默認選擇的創建虛擬環境的工具，我們就保留這個默認的選項就可以了。

項目創建完成後就可以開始新建各種文件來書寫Python代碼了，如下圖所示。左側是項目瀏覽器，可以看到剛纔創建的項目文件夾以及虛擬環境文件夾。我們可以在項目上點擊鼠標右鍵，選擇“New”，在選擇“Python File”來創建Python代碼文件，下圖中我們創建了兩個Python文件，分別是`poker_game.py`和`salary_system.py`。當然，如果願意，也可以使用複製粘貼的方式把其他地方的Python代碼文件複製到項目文件夾下。

![](./res/pycharm-workspace.png)

在工作窗口點擊鼠標右鍵可以在上下文菜單中找到“Run”選項，例如要運行`salary_system.py`文件，右鍵菜單會顯示“Run 'salary_system'”選項，點擊這個選項我們就可以運行Python代碼啦，運行結果在屏幕下方的窗口可以看到，如下圖所示。

![](res/pycharm-run-result.png)

### 常用操作和快捷鍵

PyCharm爲寫Python代碼提供了自動補全和高亮語法功能，這也是PyCharm作爲集成開發環境（IDE）的基本功能。PyCharm的“File”菜單有一個“Settings”菜單項（macOS上是在“PyCharm”菜單的“Preferences…”菜單項），這個菜單項會打開設置窗口，可以在此處對PyCharm進行設置，如下圖所示。

![](/Users/Hao/Desktop/Python-Core-50-Courses/res/pycharm-settings.png)

PyCharm的菜單項中有一個非常有用的“Code”菜單，菜單中提供了自動生成代碼、自動補全代碼、格式化代碼、移動代碼等選項，這些功能對開發者來說是非常有用的，大家可以嘗試使用這些菜單項或者記住它們對應的快捷鍵，例如在macOS上，格式化代碼這個菜單項對應的快捷鍵是`alt+command+L`。除此之外，“Refactor”菜單也非常有用，它提供了一些重構代碼的選項。所謂重構是在不改變代碼執行結果的前提下調整代碼的結構，這也是資深程序員的一項重要技能。還有一個值得一提的菜單是“VCS”，VCS是“Version Control System”（版本控制系統）的縮寫，這個菜單提供了對代碼版本管理的支持。版本控制的知識會在其他的課程中爲大家講解。

下表列出了一些PyCharm中特別常用的快捷鍵，當然如果願意，也可以通過設置窗口中“Keymap”菜單項自定義快捷鍵，PyCharm本身也針對不同的操作系統和使用習慣對快捷鍵進行了分組。

| 快捷鍵                                        | 作用                                   |
| --------------------------------------------- | -------------------------------------- |
| `command + j`                                 | 顯示可用的代碼模板                     |
| `command + b`                                 | 查看函數、類、方法的定義               |
| `ctrl + space`                                | 萬能代碼提示快捷鍵，一下不行按兩下     |
| `command + alt + l`                           | 格式化代碼                             |
| `alt + enter`                                 | 萬能代碼修復快捷鍵                     |
| `ctrl + /`                                    | 註釋/反註釋代碼                        |
| `shift + shift`                               | 萬能搜索快捷鍵                         |
| `command + d` / `command + y`                 | 複製/刪除一行代碼                      |
| `command + shift + -` / `command + shift + +` | 摺疊/展開所有代碼                      |
| `F2`                                          | 快速定位到錯誤代碼                     |
| `command+ alt + F7`                           | 查看哪些地方用到了指定的函數、類、方法 |

> **說明**：Windows系統下如果使用PyCharm的默認設置，可以將上面的`command`鍵換成`ctrl`鍵即可，唯一的例外是`ctrl + space`那個快捷鍵，因爲它跟Windows系統切換輸入法的快捷鍵是衝突的，所以在Windows系統下默認沒有與之對應的快捷鍵。