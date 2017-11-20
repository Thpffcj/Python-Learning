# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'

# 主要是用来遍历/循环 序列或者集合字典

a = [['apple', 'orange', 'banana', 'grape'], (1, 2, 3)]

for x in a:
	for y in x:
		# print(y, end='')
		if y == 'orange':
			break
		print(y)
else:
	print('fruit is gone')

# a = [1, 2, 3]
#
# for x in a:
# 	if x == 2:
# 		break
# 	print(x)
# else:
# 	print('EOF')