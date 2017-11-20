# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'

import time

def decorator(func):
	def wrapper():
		print(time.time())
		func()
	return wrapper


@decorator
def f1():
	print('This is a function f1')


@decorator
def f2():
	print('This is a function f2')


@decorator
def f3(func_name):
	print('This is a function f3 ' + func_name)

# f1 = decorator(f1)
# f2 = decorator(f2)
# f1()
# f2()

# f1()
# f2()
f3('test func')
