# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'

import re

s = 'C++JavaC#PythonC#JavascriptC#'


def convert(value):
	print(value)
	matched = value.group()
	print(matched)
	return '!!' + matched + '!!'

# s1 = s.replace('C#', 'Go')
# print(s1)

r = re.sub('C#', convert, s)
print(r)
