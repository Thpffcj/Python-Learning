# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'

# 字典来代替switch

day = 8

def get_sunday():
	return 'Sunday'

def get_monday():
	return 'Monday'

def get_tuesday():
	return 'Tuesday'

def get_default():
	return 'Unkown'

switcher = {
	0: get_sunday,
	1: get_monday,
	2: get_tuesday
}

# day_name = switcher[day]
day_name = switcher.get(day, get_default)()
print(day_name)
