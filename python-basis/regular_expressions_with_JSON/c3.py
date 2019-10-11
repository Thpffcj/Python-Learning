# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'

import re

s = 'abc, acc, adc, aec, afc, ahc'

r = re.findall('a[^cf]c', s)
r1 = re.findall('a[c-f]c', s)
print(r)
print(r1)