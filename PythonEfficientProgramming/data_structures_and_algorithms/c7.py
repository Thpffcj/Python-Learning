# _*_ coding: utf-8 _*_
__author__ = 'Thpffcj'

from collections import Counter
from random import randint

data = [randint(0, 20) for _ in range(30)]

c = Counter(data)

print(c.most_common(3))
