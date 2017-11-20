# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'

from random import randint

data = {x: randint(60, 100) for x in range(1, 21)}
print(data)

data = {k: v for k, v in data.items() if v >= 90}
print(data)
