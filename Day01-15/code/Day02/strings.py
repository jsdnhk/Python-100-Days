"""
字符串常用操作

Version: 0.1
Author: 駱昊
Date: 2018-02-27
"""

str1 = 'hello, world!'
print('字符串的長度是:', len(str1))
print('單詞首字母大寫: ', str1.title())
print('字符串變大寫: ', str1.upper())
# str1 = str1.upper()
print('字符串是不是大寫: ', str1.isupper())
print('字符串是不是以hello開頭: ', str1.startswith('hello'))
print('字符串是不是以hello結尾: ', str1.endswith('hello'))
print('字符串是不是以感嘆號開頭: ', str1.startswith('!'))
print('字符串是不是一感嘆號結尾: ', str1.endswith('!'))
str2 = '- \u9a86\u660a'
str3 = str1.title() + ' ' + str2.lower()
print(str3)
