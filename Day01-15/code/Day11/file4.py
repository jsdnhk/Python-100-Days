"""
讀寫二進制文件

Version: 0.1
Author: 駱昊
Date: 2018-03-13
"""
import base64

with open('mm.jpg', 'rb') as f:
    data = f.read()
    # print(type(data))
    # print(data)
    print('字節數:', len(data))
    # 將圖片處理成BASE-64編碼
    print(base64.b64encode(data))

with open('girl.jpg', 'wb') as f:
    f.write(data)
print('寫入完成!')
