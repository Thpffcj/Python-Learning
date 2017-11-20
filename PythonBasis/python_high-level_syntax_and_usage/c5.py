# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'

from enum import Enum
from enum import IntEnum, unique


class VIP(IntEnum):
	YELLOW = 1
	# 会报错
	# GREEN = 'str'
	BLACK = 3
	RED = 4

@unique
class VIP1(IntEnum):
	YELLOW = 1
	# GREEN = 1
	BLACK = 3
	RED = 4

