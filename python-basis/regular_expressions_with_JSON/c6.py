# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'

import re

# 边界匹配

qq = '100000001'

r = re.findall('^\d{4,8}$', qq)
r1 = re.findall('^000', qq)

print(r)
print(r1)