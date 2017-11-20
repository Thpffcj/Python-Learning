# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'

from random import randint

data = [randint(0, 20) for _ in range(30)]

c = dict.fromkeys(data, 0)

for x in data:
	c[x] += 1

print(c)
