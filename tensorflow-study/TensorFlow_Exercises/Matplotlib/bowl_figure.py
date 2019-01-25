# -*- coding: UTF-8 -*-
# Created by thpffcj on 2019-01-25.

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

"""
碗状图形
"""

fig = plt.figure(figsize=(8, 5))
ax1 = Axes3D(fig)

alpha = 0.8
r = np.linspace(-alpha, alpha, 100)
X, Y = np.meshgrid(r, r)
l = 1. / (1 + np.exp(-(X ** 2 + Y ** 2)))

ax1.plot_wireframe(X, Y, l)
ax1.plot_surface(X, Y, l, cmap=plt.get_cmap("rainbow"))  # 彩虹配色
ax1.set_title("Bowl shape")

plt.show()
