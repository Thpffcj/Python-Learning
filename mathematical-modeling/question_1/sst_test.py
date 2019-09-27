# -*- coding: UTF-8 -*-
# Created by thpffcj on 2019/9/19.
'''
    通过海洋表面温度数据绘制海洋表面温度平均温度地球图
'''

from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import pylab as mpl
from matplotlib.font_manager import FontProperties

def plot_para():#设置画图参数及相关配置,如透明度,中文啥啥的
    mpl.rcParams['axes.unicode_minus']=False
    #手动设置字体路径
    return FontProperties(fname='/Users/thpffcj/Desktop/数据挖掘/数学建模/STHeiti Medium.ttc')
file = "sst.mnmean.nc"
fh = Dataset(file, mode="r")

lons = fh.variables["lon"][:]
lats = fh.variables["lat"][:]

sst = fh.variables["sst"][1974]
sst_units = fh.variables["sst"].units

fh.close()

lon_0 = lons.mean()
lat_0 = lats.mean()

m = Basemap(projection='ortho', lat_0=45, lon_0=-100, resolution='l')

lon, lat = np.meshgrid(lons, lats)
xi, yi = m(lon, lat)

cs = m.pcolor(xi, yi, np.squeeze(sst))

# Add Grid Lines
m.drawparallels(np.arange(-90., 90., 10.), labels=[1, 0, 0, 0], fontsize=10)
m.drawmeridians(np.arange(0., 360., 10.), labels=[0, 0, 0, 1], fontsize=10)

# Add Coastlines, States, and Country Boundaries
m.drawcoastlines()
m.drawstates()
m.drawcountries()

# Add Colorbar
cbar = m.colorbar(cs, location='bottom', pad="10%")
cbar.set_label("温度(ºC)", FontProperties=plot_para())

# Add Title
plt.title('2018年7月海洋表面平均温度', FontProperties=plot_para())

# plt.show()
'''
1854-07-01 00:00:00
2018-07-01 00:00:00
'''
# plt.savefig('/Users/thpffcj/Desktop/数据挖掘/数学建模/2019年中国研究生数学建模竞赛赛题/2019年中国研究生数学建模竞赛E题/data/2018年7月海洋表面平均温度.png')