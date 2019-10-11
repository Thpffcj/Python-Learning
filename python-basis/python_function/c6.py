# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'


def print_student_files(name, gender='男', age=18, college='大学'):
	print('我叫' + name)
	print('我今年' + str(age) + '岁')
	print('我是' + gender + '生')
	print('我在' + college + '上学')

print_student_files('Thpffcj', '男', 18, '大学')
print('\r')
print_student_files('Thpffcj')
print('\r')
print_student_files('Thp', age=17)