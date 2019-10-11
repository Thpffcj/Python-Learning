# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'


def f1():
	a = 10
	def f2():
		# a此时将被pyhton认为是一个局部变量
		a = 20
		# print(a)
		return a
	# print(a)
	f2()
	# print(a)
	return f2

f = f1()
print(f)
# f2内部将a认为是局部变量，闭包为None
print(f.__closure__)
