"""
使用tkinter創建GUI
- 使用畫布繪圖
- 處理鼠標事件

Version: 0.1
Author: 駱昊
Date: 2018-03-14
"""

import tkinter


def mouse_evt_handler(evt=None):
    row = round((evt.y - 20) / 40)
    col = round((evt.x - 20) / 40)
    pos_x = 40 * col
    pos_y = 40 * row
    canvas.create_oval(pos_x, pos_y, 40 + pos_x, 40 + pos_y, fill='black')


top = tkinter.Tk()
# 設置窗口尺寸
top.geometry('620x620')
# 設置窗口標題
top.title('五子棋')
# 設置窗口大小不可改變
top.resizable(False, False)
# 設置窗口置頂
top.wm_attributes('-topmost', 1)
canvas = tkinter.Canvas(top, width=600, height=600, bd=0, highlightthickness=0)
canvas.bind('<Button-1>', mouse_evt_handler)
canvas.create_rectangle(0, 0, 600, 600, fill='yellow', outline='white')
for index in range(15):
    canvas.create_line(20, 20 + 40 * index, 580, 20 + 40 * index, fill='black')
    canvas.create_line(20 + 40 * index, 20, 20 + 40 * index, 580, fill='black')
canvas.create_rectangle(15, 15, 585, 585, outline='black', width=4)
canvas.pack()
tkinter.mainloop()

# 請思考如何用面向對象的編程思想對上面的代碼進行封裝
