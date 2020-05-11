"""
Python常用模塊
- 運行時服務相關模塊: copy / pickle / sys / ...
- 數學相關模塊: decimal / math / random / ...
- 字符串處理模塊: codecs / re / ...
- 文件處理相關模塊: shutil / gzip / ...
- 操作系統服務相關模塊: datetime / os / time / logging / io / ...
- 進程和線程相關模塊: multiprocessing / threading / queue
- 網絡應用相關模塊: ftplib / http / smtplib / urllib / ...
- Web編程相關模塊: cgi / webbrowser
- 數據處理和編碼模塊: base64 / csv / html.parser / json / xml / ...

Version: 0.1
Author: 駱昊
Date: 2018-03-05
"""

import time
import shutil
import os

seconds = time.time()
print(seconds)
localtime = time.localtime(seconds)
print(localtime)
print(localtime.tm_year)
print(localtime.tm_mon)
print(localtime.tm_mday)
asctime = time.asctime(localtime)
print(asctime)
strtime = time.strftime('%Y-%m-%d %H:%M:%S', localtime)
print(strtime)
mydate = time.strptime('2018-1-1', '%Y-%m-%d')
print(mydate)

shutil.copy('/Users/Hao/hello.py', '/Users/Hao/Desktop/first.py')
os.system('ls -l')
os.chdir('/Users/Hao')
os.system('ls -l')
os.mkdir('test')
