# -*- coding: UTF-8 -*-
# Created by thpffcj on 2019/9/19.

# from ez_setup import use_setuptools
# use_setuptools()
# import netCDF4,pydap,urllib
# import pylab,matplotlib
# import numpy as np
# dataset = netCDF4.Dataset("/Users/yuanwei/Downloads/2019年中国研究生数学建模竞赛赛题/2019年中国研究生数学建模竞赛E题/数据及程序/sst.mnmean.nc")
# print(dataset)
from netCDF4 import Dataset
import numpy as np
file = "sst.mnmean.nc"
fh = Dataset(file,mode="r")
print(fh.ncattrs())
print(fh.variables.keys())
print(fh.variables)
lons = fh.variables["lon"][:]
lats = fh.variables["lat"][:]
for i in range(0, 1800):
    tmax = fh.variables["sst"][i]

    tmax_units = fh.variables["sst"].units
    # fh.close()

    import matplotlib.pyplot as plt
    from mpl_toolkits.basemap import Basemap

    lon_0 = lons.mean()
    lat_0 = lats.mean()

    m = Basemap(projection='ortho', lat_0=45, lon_0=-100, resolution='l')

    lon, lat = np.meshgrid(lons, lats)
    xi, yi = m(lon, lat)

    cs = m.pcolor(xi, yi, np.squeeze(tmax))

    # Add Grid Lines
    m.drawparallels(np.arange(-90., 90., 10.), labels=[1, 0, 0, 0], fontsize=10)
    m.drawmeridians(np.arange(0., 360., 10.), labels=[0, 0, 0, 1], fontsize=10)

    # Add Coastlines, States, and Country Boundaries
    m.drawcoastlines()
    m.drawstates()
    m.drawcountries()

    # Add Colorbar
    cbar = m.colorbar(cs, location='bottom', pad="10%")
    cbar.set_label(tmax_units)

    # Add Title
    plt.title('DJF Maximum Temperature')

    plt.show()