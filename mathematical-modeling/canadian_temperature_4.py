# -*- coding: UTF-8 -*-
# Created by thpffcj on 2019/9/20.

import pandas as pd
import matplotlib.pyplot as plt
import pylab as mpl
from matplotlib.font_manager import FontProperties

pd.set_option('display.max_columns', 40)
pd.set_option('display.width', 1000)
def plot_para():#设置画图参数及相关配置,如透明度,中文啥啥的
    mpl.rcParams['axes.unicode_minus']=False
    #手动设置字体路径
    return FontProperties(fname='/Users/thpffcj/Desktop/数据挖掘/数学建模/STHeiti Medium.ttc')

province = pd.read_csv("Canada/Ontario/Ontario.csv")

years_province = []
data_province_3 = []
data_province_6 = []
data_province_9 = []
data_province_12 = []

interval = 3
flag = 0
month_3 = 0
month_6 = 0
month_9 = 0
month_12 = 0


for i in range(1880, 2019):
    count = province[province["Year"] == i]["Year"].count()
    if count == 12:
        month_3 += province[(province["Year"] == i) & (province["Month"] == 3)]["Mean Temp (°C)"].values
        month_6 += province[(province["Year"] == i) & (province["Month"] == 6)]["Mean Temp (°C)"].values
        month_9 += province[(province["Year"] == i) & (province["Month"] == 9)]["Mean Temp (°C)"].values
        month_12 += province[(province["Year"] == i) & (province["Month"] == 12)]["Mean Temp (°C)"].values
        flag += 1
        if flag == interval:
            month_3 = month_3 / interval
            month_6 = month_6 / interval
            month_9 = month_9 / interval
            month_12 = month_12 / interval
            years_province.append(i)
            data_province_3.append(month_3)
            data_province_6.append(month_6)
            data_province_9.append(month_9)
            data_province_12.append(month_12)
            flag = 0
            month_3 = 0
            month_6 = 0
            month_9 = 0
            month_12 = 0


plt.xlabel('时间', FontProperties=plot_para())
plt.ylabel('温度(ºC)', FontProperties=plot_para())
plt.title("Ontario同期气温变化图", FontProperties=plot_para())
plt.plot(years_province, data_province_3, label='March')
plt.plot(years_province, data_province_6, label='June')
plt.plot(years_province, data_province_9, label='September')
plt.plot(years_province, data_province_12, label='December')

plt.legend()
plt.show()
# plt.savefig('/Users/thpffcj/Desktop/数据挖掘/数学建模/2019年中国研究生数学建模竞赛赛题/2019年中国研究生数学建模竞赛E题/data/Ontario同期气温变化图.png')



