# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'


class Student():
	sum = 0
	name = 'Thp'
	age = 0

	def __init__(self, name, age):
		self.name = name
		self.age = age
		self.__score = 0
		# print(name)
		# print(age)
		# print(Student.sum)
		# self.__class__.sum += 1
		# print('当前班级学生总数为' + str(self.__class__.sum))

	def marking(self, score):
		if score < 0:
			score = 0
		self.__score = score
		print(self.name + '本次考试分数为' + str(self.__score))

	# 实例方法
	# 行为与特征
	def do_homework(self):
		self.do_english_homework()
		print('homework')

	def do_english_homework(self):
		pass

	# 类方法
	@classmethod
	def plus_sum(cls):
		cls.sum += 1
		print('当前班级学生总数为' + str(cls.sum))
		# 不能使用实例变量
		# print(self.name)

	# 静态方法
	@staticmethod
	def add(x, y):
		# print(Student.sum)
		print('This is a static method')
		# 不能使用实例变量
		# print(self.name)

student1 = Student('Thpffcj', 18)
student2 = Student('Thp', 18)

student1.marking(59)
# 利用动态给student1对象添加了新的属性__score
student1.__score = -1
print(student1.__score)
print(student1.__dict__)

# 会报错
# print(student2.__dict__)
# print(student2.__score)

# student1.add(1, 2)
# Student.add(1, 2)
# student1.plus_sum()
# Student.plus_sum()
# student2 = Student('Thp', 18)
# Student.plus_sum()
# student3 = Student('Thpff', 18)
# Student.plus_sum()