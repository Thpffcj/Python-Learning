# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'

from c5 import Human


# 继承
class Student(Human):
	# sum = 0
	def __init__(self, school, name, age):
		self.school = school
		# Human.__init__(self, name, age)
		super(Student, self).__init__(name, age)
		# self.__score = 0
		# self.__class__.sum += 1

	def do_homework(self):
		super(Student, self).do_homework()
		print('homework')

student1 = Student('大学', 'Thpffcj', 18)
student1.do_homework()
# Student.do_homework(student1)
# student1.do_homework()
# print(student1.sum)
# print(Student.sum)
# print(student1.name)
# print(student1.age)
# student1.get_name()
