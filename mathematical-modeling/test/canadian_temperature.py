# -*- coding: UTF-8 -*-
# Created by thpffcj on 2019/9/20.

import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 40)
pd.set_option('display.width', 1000)

'''
[839 rows x 25 columns]
"Date/Time","Year","Month","Mean Max Temp (°C)","Mean Max Temp Flag","Mean Min Temp (°C)","Mean Min Temp Flag","Mean Temp (°C)","Mean Temp Flag","Extr Max Temp (°C)","Extr Max Temp Flag","Extr Min Temp (°C)","Extr Min Temp Flag","Total Rain (mm)","Total Rain Flag","Total Snow (cm)","Total Snow Flag","Total Precip (mm)","Total Precip Flag","Snow Grnd Last Day (cm)","Snow Grnd Last Day Flag","Dir of Max Gust (10's deg)","Dir of Max Gust Flag","Spd of Max Gust (km/h)","Spd of Max Gust Flag"

[366 rows x 27 columns]
"Date/Time","Year","Month","Day","Data Quality","Max Temp (°C)","Max Temp Flag","Min Temp (°C)","Min Temp Flag","Mean Temp (°C)","Mean Temp Flag","Heat Deg Days (°C)","Heat Deg Days Flag","Cool Deg Days (°C)","Cool Deg Days Flag","Total Rain (mm)","Total Rain Flag","Total RaiTotal Snow (cm)","Total Snow Flag","Total Precip (mm)","Total Precip Flag","Snow on Grnd (cm)","Snow on Grnd Flag","Dir of Max Gust (10s deg)","Dir of Max Gust Flag","Spd of Max Gust (km/h)","Spd of Max Gust Flag"
'''

data_1938_2007 = pd.read_csv("卡纳达气候数据/Manitoba/WINNIPEG_1938_2007.csv", skiprows=18)

# for i in range(2009, 2010):
#     file_name = "卡纳达气候数据/Manitoba/WINNIPEG_daily_".join(str(i)).join(".csv")

file_name = "卡纳达气候数据/Manitoba/WINNIPEG_daily_2009.csv"
data = pd.read_csv(file_name, skiprows=24)

max_temp_data = data["Max Temp (°C)"]
min_temp_data = data["Min Temp (°C)"]
mean_temp_data = data["Mean Temp (°C)"]

result = pd.DataFrame(columns=["Date/Time", "Year", "Month"
                               "Mean Max Temp (°C)",
                               "Mean Min Temp (°C)",
                               "Mean Temp (°C)",
                               "Total Rain (mm)",
                               "Total Snow (cm)",
                               "Total Precip (mm)"])

# print(data)

for i in range(1, 13):
    date_time = ""
    # print(date_time)
    mean_max_temp = data[data["Month"] == i]["Max Temp (°C)"].dropna().values.mean()
    mean_min_temp = data[data["Month"] == i]["Min Temp (°C)"].dropna().values.mean()
    mean_temp = data[data["Month"] == i]["Mean Temp (°C)"].dropna().values.mean()

    total_rain = data[data["Month"] == i]["Total Rain (mm)"].dropna().values.sum()
    total_snow = data[data["Month"] == i]["Total Snow (cm)"].dropna().values.sum()
    total_precip = data[data["Month"] == i]["Total Precip (mm)"].dropna().values.sum()

print(result)

# result.to_csv('卡纳达气候数据/Manitoba/2009.csv', sep=',', header=True, index=True)


# month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
# location = 0
# for i in range(0, 12):
#     max_temp = 0.0
#     min_temp = 0.0
#     mean_temp = 0.0
#     day_not_null = 0.0
#
#     # 循环每月
#     for j in range(0, month[i]):
#         # 最高气温之和
#         if not np.isnan(max_temp_data[location]):
#             max_temp += float(max_temp_data[location])
#             day_not_null += 1
#
#         # 最低气温之和
#         if not np.isnan(min_temp_data[location]):
#             min_temp += float(min_temp_data[location])
#             day_not_null += 1
#
#         # 平均气温之和
#         if not np.isnan(mean_temp_data[location]):
#             mean_temp += float(mean_temp_data[location])
#             day_not_null += 1
#
#         location = location + 1
#
#     if day_not_null != 0:
#         max_temp = max_temp / day_not_null
#         min_temp = min_temp / day_not_null
#         mean_temp = mean_temp / day_not_null
#         print(i)
#         print(max_temp)
#         print(min_temp)
#         print(mean_temp)



