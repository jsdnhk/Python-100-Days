"""
字符串常用操作

Version: 0.1
Author: 駱昊
Date: 2018-03-19
"""

import pyperclip

# 轉義字符
print('My brother\'s name is \'007\'')
# 原始字符串
print(r'My brother\'s name is \'007\'')

str = 'hello123world'
print('he' in str)
print('her' in str)
# 字符串是否只包含字母
print(str.isalpha())
# 字符串是否只包含字母和數字
print(str.isalnum())
# 字符串是否只包含數字
print(str.isdecimal())

print(str[0:5].isalpha())
print(str[5:8].isdecimal())

list = ['牀前明月光', '疑是地上霜', '舉頭望明月', '低頭思故鄉']
print('-'.join(list))
sentence = 'You go your way I will go mine'
words_list = sentence.split()
print(words_list)
email = '     jackfrued@126.com          '
print(email)
print(email.strip())
print(email.lstrip())

# 將文本放入系統剪切板中
pyperclip.copy('老虎不發貓你當我病危呀')
# 從系統剪切板獲得文本
# print(pyperclip.paste())
