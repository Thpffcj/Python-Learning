# -*- coding: UTF-8 -*-
# Created by thpffcj on 2019/9/19.

import netCDF4
from mpl_toolkits.basemap import Basemap
import netCDF4 as nc
from netCDF4 import Dataset

nc_obj = Dataset('sst.mnmean.nc')

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
print(nc_obj.variables['time_bnds'])
print(nc_obj.variables['time'])
print(nc_obj.variables['sst'])
print('---------------------------------------')

# 查看每个变量的属性
print(nc_obj.variables['lat'].ncattrs())
print(nc_obj.variables['lon'].ncattrs())
print(nc_obj.variables['time_bnds'].ncattrs())
print(nc_obj.variables['time'].units)
print(nc_obj.variables['sst'].units)
print('---------------------------------------')

# 读取数据值
lat = (nc_obj.variables['lat'][:])
lon = (nc_obj.variables['lon'][:])
time_bnds = (nc_obj.variables['time_bnds'][:])
time = (nc_obj.variables['time'][:])
sst = (nc_obj.variables['sst'][:])

# nc.num2date(1297320, 'hours since 1800-01-01 00:00:0.0')
times = nc.num2date(time[:], 'days since 1800-01-01 00:00:0.0')
print(times[:])


# print(lat)
# print(len(lon))
# print(time_bnds)
# 它的意思是说，这些数字是从1800年1月1日00:00:00作为起始时间以小时作为计数单位累加的结果
# print(time)
# print(sst[0])
