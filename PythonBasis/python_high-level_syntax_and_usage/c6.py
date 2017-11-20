# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'

# 函数式编程
# 闭包 函数以及定义时的环境变量构成的整体

# def a():
# 	pass
#
# print(type(a))


def curve_pre():
	a = 25
	def curve(x):
		# print('This is a function')
		return a*x*x
	return curve

def curve_pre1():
	a = 30
	def curve(x):
		# print('This is a function')
		return a*x*x
	return curve

a = 10
f = curve_pre()
print(f.__closure__)
print(f.__closure__[0].cell_contents)
print(f(2))
# print(type(f))
