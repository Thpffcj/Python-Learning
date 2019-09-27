# from ez_setup import use_setuptools
# use_setuptools()
# import netCDF4,pydap,urllib
# import pylab,matplotlib
# import numpy as np
# dataset = netCDF4.Dataset("/Users/yuanwei/Downloads/2019年中国研究生数学建模竞赛赛题/2019年中国研究生数学建模竞赛E题/数据及程序/sst.mnmean.nc")
# print(dataset)
from netCDF4 import Dataset
import numpy as np
import os
os.environ["PROJ_LIB"] = "/Users/yuanwei/anaconda3/share/proj"

# file = "Data/nc/sst.mnmean.nc"
# file = "Data/nc/olr.mon.mean.nc" #每月长波辐射  #(['lon', 'olr', 'time', 'lat'])
# # file = "Data/nc/olr.mon.ltm.nc"
# fh = Dataset(file,mode="r")
# # print(fh.ncattrs())
# print(fh.variables.keys())
# print(fh.variables)
# lons = fh.variables["lon"][:]
# lats = fh.variables["lat"][:]
# tmax = fh.variables["olr"]
# time = fh.variables["time"][:]
# tmax_units = fh.variables["olr"].units
# # fh.close()
# # print(lons)
# # print(lats)
# # print(tmax)
# # print(tmax_units)
# tmp = np.array(tmax[:])
# print(tmp)
# print(time)
# print(tmp[6,:,120])
# # print(tmax[0][0][:]==tmax[0][:][0])
# print(len(tmax[0])) #[1985,88,180]
# tmax = tmax[0]
# for i in lats:
#     print(i)
# for i in lons:
#     print(i)
# import matplotlib.pyplot as plt
# from mpl_toolkits.basemap import Basemap
#
# lon_0 = lons.mean()
# lat_0 = lats.mean()
#
# m = Basemap(width=5000000,height=3500000,resolution="l",projection="stere",
#             lat_ts=40,lat_0=lat_0,lon_0=lon_0)
#
# lon,lat = np.meshgrid(lons,lats)
# xi,yi = m(lon,lat)
#
# cs = m.pcolor(xi,yi,np.squeeze(tmax))
#
# # Add Grid Lines
# m.drawparallels(np.arange(-80., 81., 10.), labels=[1,0,0,0], fontsize=10)
# m.drawmeridians(np.arange(-180., 181., 10.), labels=[0,0,0,1], fontsize=10)
#
# # Add Coastlines, States, and Country Boundaries
# m.drawcoastlines()
# m.drawstates()
# m.drawcountries()
#
# # Add Colorbar
# cbar = m.colorbar(cs, location='bottom', pad="10%")
# cbar.set_label(tmax_units)
#
# # Add Title
# plt.title('DJF Maximum Temperature')
#
# plt.show()

# import pandas as pd
# df1 = pd.read_csv("Data/Canada/Northwest_TERRITORIES/daily/FORT_SIMPSON_daily_1901_1905.csv")
# df2 = pd.read_csv("Data/Canada/Northwest_TERRITORIES/daily/FORT_SIMPSON_daily_1961_1965.csv")
# df3 = pd.read_csv("Data/Canada/Northwest_TERRITORIES/daily/FORT_SIMPSON_daily_2014_2018.csv")
# # df4 = pd.read_csv("Data/Canada/Ontario/daily/TORONTO_daily_1981_1985.csv")
# # df5 = pd.read_csv("Data/Canada/Ontario/daily/TORONTO_daily_2001_2005.csv")
# # df6 = pd.read_csv("Data/Canada/Ontario/daily/TORONTO_daily_2014_2018.csv")
# df = pd.concat([df1,df2,df3],ignore_index=True)
# df.to_csv("Data/Canada/Northwest_TERRITORIES/daily/FORT_SIMPSON_daily_1901_2018.csv",index=None)
def gs(x):
    return 0.00006*x*x-0.2093*x+195.34
print(gs(2000))
for i in range(2015,2046):
    print(gs(i))