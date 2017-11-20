# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'

ACCOUNT = 'Thpffcj'
PASSWORD = '123456'

print('please input account')
user_account = input()

print('please input password')
user_password = input()

if ACCOUNT == user_account and PASSWORD == user_password:
	print('success')
else:
	print('fail')