# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'

import re

a = 'C9C++3Java4C#5Python10Javascript'

r = re.findall('\d', a)
print(r)