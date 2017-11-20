# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'

# map 一种映射

list_x = [1, 2, 3, 4, 5, 6, 7, 8]

def square(x):
	return x * x

# for x in list_x:
# 	square(x)

r = map(square, list_x)
print(list(r))
