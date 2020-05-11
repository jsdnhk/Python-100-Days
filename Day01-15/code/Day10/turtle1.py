"""

用turtle模塊繪圖
這是一個非常有趣的模塊 它模擬一隻烏龜在窗口上爬行的方式來進行繪圖

Version: 0.1
Author: 駱昊
Date: 2018-03-14

"""

import turtle

turtle.pensize(3)
turtle.penup()
turtle.goto(-180, 150)
turtle.pencolor('red')
turtle.fillcolor('yellow')
turtle.pendown()
turtle.begin_fill()
for _ in range(36):
    turtle.forward(200)
    turtle.right(170)
turtle.end_fill()
turtle.mainloop()
