# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'

origin = 0


# def go(step):
# 	new_pos = origin + step
# 	# origin是局部变量，不会再去作用域外寻找origin
# 	origin = new_pos
# 	return origin

def go(step):
	global origin
	new_pos = origin + step
	origin = new_pos
	return new_pos

print(go(2))
print(go(3))
print(go(6))
