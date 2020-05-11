"""
使用多線程的情況 - 耗時間的任務在獨立的線程中執行

Version: 0.1
Author: 駱昊
Date: 2018-03-20
"""

import time
import tkinter
import tkinter.messagebox
from threading import Thread


def main():

    class DownloadTaskHandler(Thread):

        def run(self):
            # 模擬下載任務需要花費10秒鐘時間
            time.sleep(10)
            tkinter.messagebox.showinfo('提示', '下載完成!')
            # 啓用下載按鈕
            button1.config(state=tkinter.NORMAL)

    def download():
        # 禁用下載按鈕
        button1.config(state=tkinter.DISABLED)
        # 通過daemon參數將線程設置爲守護線程(主程序退出就不再保留執行)
        DownloadTaskHandler(daemon=True).start()

    def show_about():
        tkinter.messagebox.showinfo('關於', '作者: 駱昊(v1.0)')

    top = tkinter.Tk()
    top.title('單線程')
    top.geometry('200x150')
    top.wm_attributes('-topmost', 1)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='下載', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='關於', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()


if __name__ == '__main__':
    main()
