"""
擲骰子決定做什麼事情

Version: 0.1
Author: 駱昊
Date: 2018-02-28
"""
from random import randint

face = randint(1, 6)
if face == 1:
    result = '唱首歌'
elif face == 2:
    result = '跳個舞'
elif face == 3:
    result = '學狗叫'
elif face == 4:
    result = '做俯臥撐'
elif face == 5:
    result = '念繞口令'
else:
    result = '講冷笑話'
print(result)
