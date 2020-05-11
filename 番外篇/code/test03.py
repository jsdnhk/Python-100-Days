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