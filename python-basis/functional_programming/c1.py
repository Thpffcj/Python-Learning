# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'

# 匿名函数

def add(x, y):
	return x + y

# print(add(1, 2))

f = lambda x, y: x+y
# print(f(1, 2))

a = 2
b = 1
result = a if a > b else b
print(result)
