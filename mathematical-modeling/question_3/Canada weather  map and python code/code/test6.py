import numpy as np
import netCDF4 as nc

file_path = 'e:/localpython/sm/sst.mnmean.nc'
file_obj = nc.Dataset(file_path)

print('0------------------------')
print(file_obj)
print()

#-------------------------------------------------------------
print('1------------------------')
print(file_obj.variables.keys())
print()

print('2------------------------')
lat = file_obj.variables['lat']
print(lat)
print()

print('3------------------------')
lon = file_obj.variables['lon']
print(lon)
print()

print('4------------------------')
time_bnds = file_obj.variables['time_bnds']
print(time_bnds)
print()

print('5------------------------')
time = file_obj.variables['time']
print(time)
print()

print('6------------------------')
sst = file_obj.variables['sst']
print(sst)
print()
#-------------------------------------------------------------

