# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'

from random import randint

data = [randint(-10, 10) for _ in range(10)]
print(data)

# data = filter(lambda x: x >= 0, data)
# print(list(data))

# 列表解析比filter快
data = [x for x in data if x >= 0]
print(data)
