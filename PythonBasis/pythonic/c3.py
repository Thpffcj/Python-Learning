# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'

students = {
	'喜小乐': 18,
	'石敢当': 20,
	'冯小五': 15
}

b = (key for key, value in students.items())
b1 = [key for key, value in students.items()]
b2 = {value: key for key, value in students.items()}

# print(b)
for x in b:
	print(x)
