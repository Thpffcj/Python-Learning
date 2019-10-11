# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'

from enum import Enum


class VIP(Enum):
	YELLOW = 1
	GREEN = 2
	BLACK = 3
	RED = 4


class VIP1(Enum):
	YELLOW = 1
	GREEN = 2
	BLACK = 3
	RED = 4

# 没有不等于比较
# result = VIP.GREEN < VIP.BLACK
result1 = VIP.GREEN is VIP.GREEN
result2 = VIP.GREEN == VIP1.GREEN

# print(result)
print(result1)
print(result2)
