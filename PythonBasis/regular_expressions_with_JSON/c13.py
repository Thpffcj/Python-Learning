# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'

import json

json_str = '[{"name" : "Thpffcj", "age" : 18, "flag" : false}, {"name" : "Thpffcj", "age" : 18}]'

# 反序列化 字符串到语言中的某种数据结构
student = json.loads(json_str)

print(type(student))
print(student)
# print(student['name'], student['age'])
print(student[0]['name'])