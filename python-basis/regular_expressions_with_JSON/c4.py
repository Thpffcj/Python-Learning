# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'

import re

# \d \D
# \w 单词字符 \W
# \s 空白字符 \S

s = 'python 1111\njava\r&678php\t'

r = re.findall('\s', s)
print(r)
