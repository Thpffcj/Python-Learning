# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'

from enum import Enum


# 枚举
class VIP(Enum):
	YELLOW = 1
	GREEN = 2
	BLACK = 3
	RED = 4

print(VIP.YELLOW)
# 不可更改
# VIP.YELLOW = 6
