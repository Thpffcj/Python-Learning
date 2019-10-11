# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'

import time

# 装饰器
# 对修改是封闭的，对扩展是开放的

def f1():
	# print(time.time())
	print('This is a function f1')


def f2():
	print('This is a function f2')


def print_current_tine(func):
	print(time.time())
	func()

print_current_tine(f1)
print_current_tine(f2)
