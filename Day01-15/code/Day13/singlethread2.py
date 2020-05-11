"""
不使用多線程的情況 - 耗時間的任務阻塞主事件循環

Version: 0.1
Author: 駱昊
Date: 2018-03-20
"""

import time
import tkinter
import tkinter.messagebox


def download():
    # 模擬下載任務需要花費10秒鐘時間
    time.sleep(10)
    tkinter.messagebox.showinfo('提示', '下載完成!')


def show_about():
    tkinter.messagebox.showinfo('關於', '作者: 駱昊(v1.0)')


def main():
    top = tkinter.Tk()
    top.title('單線程')
    top.geometry('200x150')
    top.wm_attributes('-topmost', True)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='下載', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='關於', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()


if __name__ == '__main__':
    main()


# 在不使用多線程的情況下 一旦點擊下載按鈕 由於該操作需要花費10秒中的時間
# 整個主消息循環也會被阻塞10秒鐘無法響應其他的事件
# 事實上 對於沒有因果關係的子任務 這種順序執行的方式並不合理
