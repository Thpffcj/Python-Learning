# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'

import re

s = 'C++JavaC#\nPythonJavascript'

r = re.findall('c#.{1}', s, re.I)
r1 = re.findall('c#.{1}', s, re.I | re.S)

print(r)
print(r1)