# -*- coding: UTF-8 -*-
# Created by thpffcj on 2019/9/19.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# 运用 Basemap 函数我们可以在绘图区域中绘制地理信息相关的图像，当参数 projection 的值为 'ortho' #时，我们将得到一个如下所示的地球仪截面：

plt.figure(figsize=(8, 8))
m = Basemap(projection='ortho', resolution=None, lat_0=50, lon_0=-100)
m.bluemarble(scale=0.5)
plt.show()

fig = plt.figure(figsize=(8, 8))
m = Basemap(projection='lcc', resolution=None,
            width=8E6, height=8E6,
            lat_0=45, lon_0=-100, )
m.etopo(scale=0.5, alpha=0.5)

# 将经纬度映射为 (x, y) 坐标，用于绘制图像
x, y = m(-122.3, 47.6)
plt.plot(x, y, 'ok', markersize=5)
plt.text(x, y, ' Seattle', fontsize=12)
plt.show()