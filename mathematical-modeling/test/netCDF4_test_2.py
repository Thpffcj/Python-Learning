# -*- coding: UTF-8 -*-
# Created by thpffcj on 2019/9/19.

import netCDF4
from mpl_toolkits.basemap import Basemap
import netCDF4 as nc
from netCDF4 import Dataset

nc_obj = Dataset('air.2x2.250.mon.anom.land.nc')

# 查看nc文件有些啥东东
print(nc_obj)
print('---------------------------------------')

# 查看nc文件中的变量
print(nc_obj.variables.keys())
for i in nc_obj.variables.keys():
    print(i)
print('---------------------------------------')

# 查看每个变量的信息
print(nc_obj.variables['lat'])
print(nc_obj.variables['lon'])
print(nc_obj.variables['time'])
print(nc_obj.variables['air'])
print('---------------------------------------')

lat = (nc_obj.variables['lat'][:])
lon = (nc_obj.variables['lon'][:])
time = (nc_obj.variables['time'][:])
air = (nc_obj.variables['air'][:])
print(air)
