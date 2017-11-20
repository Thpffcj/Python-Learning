# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'

data = {2, 2, -3, -5, 9, 6, 7, 5, 8, 7}
print(data)

data = {x for x in data if x%3 ==0}
print(data)
