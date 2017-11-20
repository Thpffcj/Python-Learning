# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'

list_x = [1, 0, 1, 0, 0, 1]
list_u = ['a', 'B', 'c', 'F', 'e']

# r = filter(lambda x: True if x == 1 else False, list_x)
r = filter(lambda x: x, list_x)
r1 = filter(lambda x: True if x > 'A' and x < 'Z' else False, list_u)

print(list(r))
print(list(r1))