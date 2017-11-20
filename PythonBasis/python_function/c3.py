# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'


def damage(skill1, skill2):
	damage1 = skill1 * 3
	damage2 = skill2 * 2 + 10
	return damage1, damage2


skill1_damage, skill2_damage = damage(3, 6)
print(skill1_damage, skill2_damage)
