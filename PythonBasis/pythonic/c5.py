# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'

class Test():

	def __bool__(self):
		return True

	def __len__(self):
		return 0


test = Test()

print(bool(None))
print(bool([]))
print(bool(test))

if test:
	print('S')
else:
	print('F')
