import numpy as np
import netCDF4 as nc

file_path = 'e:/localpython/sm/X202.119.44.230.263.21.8.25.nc'
file_obj = nc.Dataset(file_path)

print('0------------------------')
print(file_obj)
print()

#-------------------------------------------------------------
print('01------------------------')
print(file_obj.variables.keys())
print()


print('1------------------------')
lat = file_obj.variables['lat']
print(lat)
print()

print('2------------------------')
lon = file_obj.variables['lon']
print(lon)
print()

print('3------------------------')
time = file_obj.variables['time']
print(time)
print(time[:])
print(time.units)
times = nc.num2date(time[:], time.units)
print(times)
print()

'''
print('4------------------------')
climatology_bounds = file_obj.variables['climatology_bounds']
print(climatology_bounds)
print()

print('5------------------------')
tmax = file_obj.variables['tmax']
print(tmax)
print()

print('6------------------------')
not_missing_count = file_obj.variables['not_missing_count']
print(not_missing_count)
print()
#-------------------------------------------------------------

#print(file_obj.variables["time"][:])
'''


lons = file_obj.variables["lon"][:]
#print(lons)
lats = file_obj.variables["lat"][:]
#print(lats)
#t_max = file_obj.variables["tmax"][0]
#print(t_max)
#tmax = file_obj.variables["tmax"][:]
#print(type(tmax))
tmax = file_obj.variables["tmax"][:]
print(len(tmax.mean(axis=0)))
tmax = tmax.mean(axis=0)
print(tmax)
#print(len(tmax.mean(axis=1)))
tmax_units = file_obj.variables["tmax"].units
file_obj.close()

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

#m = Basemap(resolution="l",projection="ortho",
 #           lat_0=45,lon_0=-100)


lon_0 = lons.mean()
lat_0 = lats.mean()
m = Basemap(width=6800000,height=5500000,resolution="l",projection="stere",
            lat_ts=40,lat_0=lat_0,lon_0=lon_0)

lon,lat = np.meshgrid(lons,lats)
xi,yi = m(lon,lat)

cs = m.pcolor(xi,yi,np.squeeze(tmax))

# Add Grid Lines
m.drawparallels(np.arange(-80., 81., 10.), labels=[1,0,0,0], fontsize=10)
m.drawmeridians(np.arange(0., 360., 10.), labels=[0,0,0,1], fontsize=10)

# Add Coastlines, States, and Country Boundaries
m.drawcoastlines()
m.drawstates()
m.drawcountries()

# Add Colorbar
cbar = m.colorbar(cs, location='bottom', pad="10%")
cbar.set_label(tmax_units)

# Add Title
plt.title('DJF Maximum Temperature')
plt.savefig('e:/localpython/sm/temp.png')
plt.show()
