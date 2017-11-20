# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'


# 类最基本的作用：封装

class Student():
	# 类变量
	sum = 0

	# 构造函数
	def __init__(self, name, age):
		# 初始化对象的属性
		# 实例变量
		self.name = name
		self.age = age
		# print('student')

	def do_homework(self):
		print('homework')


class StudentHomework():
	homework_name = ''


# class Printer():
# 	def print_file(self):
# 		print('name: ' + self.name)
# 		print('age: ' + str(self.age))


student1 = Student('Thpffcj', 18)
student2 = Student('Thpffcj1', 19)
print(student1.name)
print(student2.name)
print(Student.sum)
print(student1.__dict__)
print(Student.__dict__)
# student2 = Student()
# student3 = Student()

# print(id(student1))
# print(id(student2))
# print(id(student3))

# student1.print_file()
