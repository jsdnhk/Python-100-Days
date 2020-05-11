"""

使用tkinter創建GUI
- 在窗口上製作動畫

Version: 0.1
Author: 駱昊
Date: 2018-03-14

"""

import tkinter
import time


# 播放動畫效果的函數
def play_animation():
    canvas.move(oval, 2, 2)
    canvas.update()
    top.after(50, play_animation)


x = 10
y = 10
top = tkinter.Tk()
top.geometry('600x600')
top.title('動畫效果')
top.resizable(False, False)
top.wm_attributes('-topmost', 1)
canvas = tkinter.Canvas(top, width=600, height=600, bd=0, highlightthickness=0)
canvas.create_rectangle(0, 0, 600, 600, fill='gray')
oval = canvas.create_oval(10, 10, 60, 60, fill='red')
canvas.pack()
top.update()
play_animation()
tkinter.mainloop()

# 請思考如何讓小球碰到屏幕的邊界就彈回
# 請思考如何用面向對象的編程思想對上面的代碼進行封裝
