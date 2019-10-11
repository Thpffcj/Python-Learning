# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'

import re

s = 'A85C37F21D86'

def convert(value):
	matched = value.group()
	if int(matched) >= 6:
		return '9'
	else:
		return '0'

r = re.sub('\d', convert, s)

print(r)