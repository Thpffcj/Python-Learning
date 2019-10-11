# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'

# 正则表达式是一个特殊的字符序列，一个字符串是否与我们所设定的这样的字符序列，相匹配。

# 快速检索文本，实现一些替换文本的操作

# 1. 检测一串数字是否是电话号码
# 2. 检测一个字符串是否符合email
# 3. 把一个文本里指定的单词替换为另外一个单词

import re

a = 'C|C++|Java|C#|Python|Javascript'

# print(a.index('Python') > -1)
# print('Python' in a)

r = re.findall('Python', a)
if len(r) > 0:
	print('字符串中包含Python')
else:
	print('No')