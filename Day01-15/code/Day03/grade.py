"""
百分制成績轉等級製成績
90分以上，輸出A
80分~89分，輸出B
70分~79分，輸出C
60分~69分，輸出D
60分以下，輸出E

Version: 0.1
Author: 駱昊
Date: 2018-02-28
"""

score = float(input('請輸入成績: '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print('對應的等級是:', grade)
