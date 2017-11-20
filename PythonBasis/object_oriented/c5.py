# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'


class Human():

	sum = 0

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def get_name(self):
		print(self.name)

	def do_homework(self):
		print('This is parent method')


