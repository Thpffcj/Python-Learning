import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pylab as mpl
#解决不能显示中文的问题
mpl.rcParams["font.sans-serif"] = ["FangSong"]
mpl.rcParams["axes.unicode_minus"] = False

data = pd.read_csv("Data/Canada/Alberta/CALGARY_daily_2014.csv", skiprows=24)
data2 = pd.read_csv("Data/Canada/British_Columbia/VANCOUVER_daily_2014.csv", skiprows=24)
pd.set_option('display.max_columns', 40)
pd.set_option('display.width', 1000)
# print(data)
# print(data["Max Temp (°C)"]) #选取某列
# print(data[data["Month"]==1])  #选取为1月的列
# max_temp = data["Max Temp (°C)"].values
# max_temp2 = data2["Max Temp (°C)"].values
# print(len(max_temp))
# print(len(max_temp2))
# x = np.arange(1,len(max_temp)+1)
# print(len(x))
calgary_1881_2012 = pd.read_csv("Data/Canada/Alberta/CALGARY_1881_2012.csv", skiprows=18)
calgary_2014 = pd.read_csv("Data/Canada/Alberta/CALGARY_daily_2013.csv",skiprows=24)
print(calgary_1881_2012.head())
print(calgary_2014.head())
print(calgary_1881_2012.keys())
print(calgary_2014.keys())
print(set(calgary_2014.keys()).intersection(set(calgary_1881_2012.keys())))
print(calgary_1881_2012.dtypes)
tmp = ["Date/Time","Year","Month","Mean Max Temp (°C)","Mean Min Temp (°C)","Mean Temp (°C)","Total Rain (mm)","Total Snow (cm)","Total Precip (mm)"]
print(len(set(calgary_2014.keys()).intersection(set(tmp))))
print(len(tmp))
print("Snow Grnd Last Day (cm)" in calgary_2014.keys())
#daily里面差的是三个Mean
#第一步，先把monthly文件调整为标准样式
#["Date/Time","Year","Month","Mean Max Temp (°C)","Mean Min Temp (°C)","Mean Temp (°C)","Total Rain (mm)","Total Snow (cm)","Total Precip (mm)"]
print(calgary_1881_2012[tmp])
# calgary_1881_2012[tmp].to_csv("Data/Canada/Alberta/CALGARY_1881_2012_standard.csv",index=None)

#第二步，计算daily中的平均值

date_time = []
year = []
month = []
mean_max_temp = []
mean_min_temp = []
mean_mean_temp = []
total_rain = []
total_snow = []
total_preceip = []
import datetime
# print(datetime.datetime.strptime("2011-1","%Y-%m"))
for i in range(1,13):
    date_time.append("%d-%d"%(2014,i))
    year.append(2014)
    month.append(i)
    mean_max_temp.append(calgary_2014[calgary_2014["Month"] == i]["Max Temp (°C)"].dropna().values.mean())
    mean_min_temp.append(calgary_2014[calgary_2014["Month"] == i]["Min Temp (°C)"].dropna().values.mean())
    mean_mean_temp.append(calgary_2014[calgary_2014["Month"] == i]["Mean Temp (°C)"].dropna().values.mean())
    total_rain.append(calgary_2014[calgary_2014["Month"] == i]["Total Rain (mm)"].dropna().values.sum())
    total_snow.append(calgary_2014[calgary_2014["Month"] == i]["Total Snow (cm)"].dropna().values.sum())
    total_preceip.append(calgary_2014[calgary_2014["Month"] == i]["Total Precip (mm)"].dropna().values.sum())
print(len(tmp))
# print(len([date_time,year,month,mean_max_temp,mean_min_temp,mean_mean_temp,total_rain,total_snow,total_preceip]))
t = dict(zip(tmp,[date_time,year,month,mean_max_temp,mean_min_temp,mean_mean_temp,total_rain,total_snow,total_preceip]))

calgary_2014_new = pd.DataFrame(t)
print(calgary_2014_new)
calgary_2014_new.to_csv("Data/Canada/Alberta/CALGARY_daily_2013_standard.csv",index=None)
print(pd.read_csv("Data/Canada/Alberta/CALGARY_daily_2013_standard.csv").head())



#显示两个城市的每日最高气温图
# plt.plot(x,max_temp,label="CALGARY")
# plt.plot(x,max_temp2,label="VANCOUVER")
# plt.xlabel("day")
# plt.ylabel("°C")
# plt.title("2014各城市每日最高气温")
# print(data["Max Temp (°C)"][40:70])
# plt.legend()
# plt.show()

#显示两个城市每月平均最高气温
# calgary_data = []
# vancouver_data = []
# # print(data[data["Month"]==1]["Max Temp (°C)"]) #一月最高气温
# for i in range(1,13):
#     calgary_data.append(data[data["Month"]==i]["Max Temp (°C)"].values.mean())
#     vancouver_data.append(data2[data2["Month"]==i]["Max Temp (°C)"].dropna().values.mean())
# x = np.arange(1,13)
# plt.plot(x,calgary_data,label="CALGARY")
# plt.plot(x,vancouver_data,label="VANCOUVER")
# print(vancouver_data)
# plt.xlabel("month")
# plt.ylabel("°C")
# plt.legend()
# plt.show()





