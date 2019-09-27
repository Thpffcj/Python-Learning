import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['KaiTi']
x = range(30)
l1 = plt.plot(x, x, 'ro')
l2 = plt.plot(x, [y ** 2 for y in x], 'bs')
l3 = plt.plot(x, [y ** 3 for y in x], 'g^')
plt.title('不同线性测试')
plt.xlabel('x坐标轴标签')
plt.ylabel('y轴坐标标签')
plt.legend((l1[0], l2[0], l3[0]), ('1', '2', '3'))
plt.show()