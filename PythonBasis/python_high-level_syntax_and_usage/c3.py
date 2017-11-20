# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'

from enum import Enum


class VIP(Enum):
	YELLOW = 1
	# 别名
	YELLOW_ALIAS = 1
	GREEN = 2
	BLACK = 3
	RED = 4

# 枚举类型 枚举的名字 枚举的值
# print(type(VIP.YELLOW))
# print(VIP.YELLOW.name)
# print(VIP.YELLOW.value)
# print(VIP['GREEN'])

a = 1
print(VIP(a))

# 获得每一种枚举类型
# for v in VIP:
# 	print(v)
#
# for v in VIP.__members__.items():
# 	print(v)
