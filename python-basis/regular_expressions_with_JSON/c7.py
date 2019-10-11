# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'

import re

s = 'PythonPythonPythonPythonPythonPython'

r = re.findall('(Python){3}', s)

print(r)