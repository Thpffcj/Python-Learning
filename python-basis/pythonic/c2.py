# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'

# 列表推导式

a = [1, 2, 3, 4, 5, 6, 7, 8]

b = [i**2 for i in a if i >= 5]

print(b)

a1 = {1, 2, 3, 4, 5, 6, 7, 8}

b1 = {i**2 for i in a if i >= 5}

print(b1)
