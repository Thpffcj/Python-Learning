# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'

from functools import reduce

# 连续计算，连续调用lambda表达式
list_x = ['1', '2', '3', '4', '5', '6', '7', '8']
r = reduce(lambda x, y: x + y, list_x, 'a')

print(r)

# map/reduce 编程模型 映射 规约 并行计算
