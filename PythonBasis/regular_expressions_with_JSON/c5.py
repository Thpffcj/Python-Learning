# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'

import re

# 数量词
# * 匹配0次或无限多次
# + 匹配1次或无限多次
# ? 匹配0次或1次

s = 'python 1111java678php'
s1 = 'pytho0python1pythonn2'

# 贪婪与非贪婪
r = re.findall('[a-z]{3,6}?', s)
r1 = re.findall('python*', s1)
r2 = re.findall('python+', s1)
r3 = re.findall('python?', s1)
r4 = re.findall('python{1,2}', s1)
r5 = re.findall('python{1,2}?', s1)
# print(r)
print(r1)
print(r2)
print(r3)
print(r4)
print(r5)