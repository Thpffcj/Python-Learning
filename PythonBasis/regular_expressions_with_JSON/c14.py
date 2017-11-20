# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'

import json

# json     python
# object   dict
# array    list
# string   str
# number   int
# number   float
# true     True
# false    False
# null     None

# 序列化
student = [
	{'name': 'Thpffcj', 'age': 18, 'flag': False},
	{'name': 'Thpffcj', 'age': 18}
]

json_str = json.dumps(student)
print(type(json_str))
print(json_str)