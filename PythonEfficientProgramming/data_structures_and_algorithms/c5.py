# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'

from collections import namedtuple

Studnet = namedtuple('Studnet', ['name', 'age', 'sex', 'email'])

s = Studnet('Jim', 16, 'mail', 'jim8721@gmail.com')

print(s)
print(s.name)
print(isinstance(s, tuple))
