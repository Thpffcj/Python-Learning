# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'

import re

s = 'A85C37F21D86'
s1 = '5A85C37F21D86'

r = re.findall('\d', s1)

# 从字符串的首字母开始匹配直到第一个满足正则表达的结果
r1 = re.match('\d', s1)

# 将搜索整个字符串直到第一个满足正则表达的结果
r2 = re.search('\d', s1)

print(r)
print(r1.span())
print(r2.group())