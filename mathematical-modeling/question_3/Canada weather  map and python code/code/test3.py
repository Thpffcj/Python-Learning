# from ez_setup import use_setuptools
# use_setuptools()
# import netCDF4,pydap,urllib
# import pylab,matplotlib
# import numpy as np
# dataset = netCDF4.Dataset("/Users/yuanwei/Downloads/2019年中国研究生数学建模竞赛赛题/2019年中国研究生数学建模竞赛E题/数据及程序/sst.mnmean.nc")
# print(dataset)
from netCDF4 import Dataset
import numpy as np
file = "e:/localpython/sm/X202.119.44.230.263.21.30.26.nc"
fh = Dataset(file,mode="r")
print("start--------------------------------------------------")
print()
print("fh.ncattrs()--------------------------------------------------")
print(fh.ncattrs())
print()
print("fh.variables.keys()--------------------------------------------------")
print(fh.variables.keys())
print()
print("fh.variables--------------------------------------------------")
print(fh.variables)
print()
print("end")
print()

print(fh.variables["time"][:])

lons = fh.variables["lon"][:]
#print(lons)
lats = fh.variables["lat"][:]
#print(lats)
tmax = fh.variables["icec"][0]

tmax_units = fh.variables["icec"].units
fh.close()

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

lon_0 = lons.mean()
lat_0 = lats.mean()

#m = Basemap(resolution="l",projection="ortho",
#            lat_0=45,lon_0=-100)
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

plt.show()
