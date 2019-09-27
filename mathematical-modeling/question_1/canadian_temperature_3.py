# -*- coding: UTF-8 -*-
# Created by thpffcj on 2019/9/20.

'''
    绘制加拿大13个区域历史温度变化情况
'''

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


alberta = pd.read_csv("Canada/Alberta/alberta.csv")
british_columbia = pd.read_csv("Canada/British_Columbia/British_Columbia.csv")
manitoba = pd.read_csv("Canada/Manitoba/Manitoba.csv")
new_brunswick = pd.read_csv("Canada/New_Brunswick/New_Brunswick.csv")
newfoundland_labrador = pd.read_csv("Canada/Newfoundland_Labrador/Newfoundland_Labrador.csv")
northwest_TERRITORIES = pd.read_csv("Canada/Northwest_TERRITORIES/Northwest_TERRITORIES.csv")
nova_scotia = pd.read_csv("Canada/Nova_Scotia/Nova_Scotia.csv")
nunavut = pd.read_csv("Canada/Nunavut/Nunavut.csv")
ontario = pd.read_csv("Canada/Ontario/Ontario.csv")
prince_edward_island = pd.read_csv("Canada/Prince_Edward_Island/Prince_Edward_Island.csv")
quebec = pd.read_csv("Canada/Quebec/Quebec.csv")
saskatchewan = pd.read_csv("Canada/Saskatchewan/Saskatchewan.csv")
yukon = pd.read_csv("Canada/Yukon/Yukon.csv")

years_alberta = []
data_alberta = []
years_british_columbia = []
data_british_columbia = []
years_manitoba = []
data_manitoba = []
years_new_brunswick = []
data_new_brunswick = []
years_newfoundland_labrador = []
data_newfoundland_labrador = []
years_northwest_TERRITORIES = []
data_northwest_TERRITORIES = []
years_nova_scotia = []
data_nova_scotia = []
years_nunavut = []
data_nunavut = []
years_ontario = []
data_ontario = []
years_prince_edward_island = []
data_prince_edward_island = []
years_quebec = []
data_quebec = []
years_saskatchewan = []
data_saskatchewan = []
years_yukon = []
data_yukon = []

alberta_mean = 0.0
british_columbia_mean = 0.0
manitoba_mean = 0.0
new_brunswick_mean = 0.0
newfoundland_labrador_mean = 0.0
northwest_TERRITORIES_mean = 0.0
nova_scotia_mean = 0.0
nunavut_mean = 0.0
ontario_mean = 0.0
prince_edward_island_mean = 0.0
quebec_mean = 0.0
saskatchewan_mean = 0.0
yukon_mean = 0.0

interval = 2

flag = 0
# alberta
for i in range(1880, 2019):
    count = alberta[alberta["Year"] == i]["Year"].count()
    if count == 12:
        alberta_mean += alberta[alberta["Year"] == i]["Mean Temp (°C)"].values.mean()
        flag += 1
        if flag == interval:
            alberta_mean = alberta_mean / interval
            years_alberta.append(i)
            data_alberta.append(alberta_mean)
            flag = 0
            alberta_mean = 0

flag = 0
# british_columbia
for i in range(1937, 2019):
    count = british_columbia[british_columbia["Year"] == i]["Year"].count()
    if count == 12:
        british_columbia_mean += british_columbia[british_columbia["Year"] == i]["Mean Temp (°C)"].values.mean()
        flag += 1
        if flag == interval:
            british_columbia_mean = british_columbia_mean / interval
            years_british_columbia.append(i)
            data_british_columbia.append(british_columbia_mean)
            flag = 0
            british_columbia_mean = 0

flag = 0
# manitoba
for i in range(1938, 2019):
    count = manitoba[manitoba["Year"] == i]["Year"].count()
    if count == 12:
        manitoba_mean += manitoba[manitoba["Year"] == i]["Mean Temp (°C)"].values.mean()
        flag += 1
        if flag == interval:
            manitoba_mean = manitoba_mean / interval
            years_manitoba.append(i)
            data_manitoba.append(manitoba_mean)
            flag = 0
            manitoba_mean = 0

flag = 0
# new_brunswick
for i in range(1871, 2019):
    count = new_brunswick[new_brunswick["Year"] == i]["Year"].count()
    if count == 12:
        new_brunswick_mean += new_brunswick[new_brunswick["Year"] == i]["Mean Temp (°C)"].values.mean()
        flag += 1
        if flag == interval:
            new_brunswick_mean = new_brunswick_mean / interval
            years_new_brunswick.append(i)
            data_new_brunswick.append(new_brunswick_mean)
            flag = 0
            new_brunswick_mean = 0

flag = 0
# newfoundland_labrador
for i in range(1937, 2019):
    count = newfoundland_labrador[newfoundland_labrador["Year"] == i]["Year"].count()
    if count == 12:
        newfoundland_labrador_mean += newfoundland_labrador[newfoundland_labrador["Year"] == i]["Mean Temp (°C)"].values.mean()
        flag += 1
        if flag == interval:
            newfoundland_labrador_mean = newfoundland_labrador_mean / interval
            years_newfoundland_labrador.append(i)
            data_newfoundland_labrador.append(newfoundland_labrador_mean)
            flag = 0
            newfoundland_labrador_mean = 0

flag = 0
# northwest_TERRITORIES
for i in range(1895, 2019):
    count = northwest_TERRITORIES[northwest_TERRITORIES["Year"] == i]["Year"].count()
    if count == 12:
        northwest_TERRITORIES_mean += northwest_TERRITORIES[northwest_TERRITORIES["Year"] == i]["Mean Temp (°C)"].values.mean()
        flag += 1
        if flag == interval:
            northwest_TERRITORIES_mean = northwest_TERRITORIES_mean / interval
            years_northwest_TERRITORIES.append(i)
            data_northwest_TERRITORIES.append(northwest_TERRITORIES_mean)
            flag = 0
            northwest_TERRITORIES_mean = 0

flag = 0
# nova_scotia
for i in range(1870, 2019):
    count = nova_scotia[nova_scotia["Year"] == i]["Year"].count()
    if count == 12:
        nova_scotia_mean += nova_scotia[nova_scotia["Year"] == i]["Mean Temp (°C)"].values.mean()
        flag += 1
        if flag == interval:
            nova_scotia_mean = nova_scotia_mean / interval
            years_nova_scotia.append(i)
            data_nova_scotia.append(nova_scotia_mean)
            flag = 0
            nova_scotia_mean = 0

flag = 0
# nunavut
for i in range(1929, 2019):
    count = nunavut[nunavut["Year"] == i]["Year"].count()
    if count == 12:
        nunavut_mean += nunavut[nunavut["Year"] == i]["Mean Temp (°C)"].values.mean()
        flag += 1
        if flag == interval:
            nunavut_mean = nunavut_mean / interval
            years_nunavut.append(i)
            data_nunavut.append(nunavut_mean)
            flag = 0
            nunavut_mean = 0

flag = 0
# ontario
for i in range(1840, 2019):
    count = ontario[ontario["Year"] == i]["Year"].count()
    if count == 12:
        ontario_mean += ontario[ontario["Year"] == i]["Mean Temp (°C)"].values.mean()
        flag += 1
        if flag == interval:
            ontario_mean = ontario_mean / interval
            years_ontario.append(i)
            data_ontario.append(ontario_mean)
            flag = 0
            ontario_mean = 0

flag = 0
# prince_edward_island
for i in range(1872, 2019):
    count = prince_edward_island[prince_edward_island["Year"] == i]["Year"].count()
    if count == 12:
        prince_edward_island_mean += prince_edward_island[prince_edward_island["Year"] == i]["Mean Temp (°C)"].values.mean()
        flag += 1
        if flag == interval:
            prince_edward_island_mean = prince_edward_island_mean / interval
            years_prince_edward_island.append(i)
            data_prince_edward_island.append(prince_edward_island_mean)
            flag = 0
            prince_edward_island_mean = 0

flag = 0
# quebec
for i in range(1928, 2019):
    count = quebec[quebec["Year"] == i]["Year"].count()
    if count == 12:
        quebec_mean += quebec[quebec["Year"] == i]["Mean Temp (°C)"].values.mean()
        flag += 1
        if flag == interval:
            quebec_mean = quebec_mean / interval
            years_quebec.append(i)
            data_quebec.append(quebec_mean)
            flag = 0
            quebec_mean = 0

flag = 0
# saskatchewan
for i in range(1928, 2019):
    count = saskatchewan[saskatchewan["Year"] == i]["Year"].count()
    if count == 12:
        saskatchewan_mean += saskatchewan[saskatchewan["Year"] == i]["Mean Temp (°C)"].values.mean()
        flag += 1
        if flag == interval:
            saskatchewan_mean = saskatchewan_mean / interval
            years_saskatchewan.append(i)
            data_saskatchewan.append(saskatchewan_mean)
            flag = 0
            saskatchewan_mean = 0

flag = 0
# saskatchewan
for i in range(1897, 2019):
    count = yukon[yukon["Year"] == i]["Year"].count()
    if count == 12:
        yukon_mean += yukon[yukon["Year"] == i]["Mean Temp (°C)"].values.mean()
        flag += 1
        if flag == interval:
            yukon_mean = yukon_mean / interval
            years_yukon.append(i)
            data_yukon.append(yukon_mean)
            yukon_mean = 0

plt.plot(years_alberta, data_alberta, label='Alberta')
plt.plot(years_british_columbia, data_british_columbia, label='British Columbia')
plt.plot(years_manitoba, data_manitoba, label='Manitoba')
plt.plot(years_new_brunswick, data_new_brunswick, label='New Brunswick')
plt.plot(years_newfoundland_labrador, data_newfoundland_labrador, label='Newfoundland Labrador')
plt.plot(years_northwest_TERRITORIES, data_northwest_TERRITORIES, label='Northwest Territories')
plt.plot(years_nova_scotia, data_nova_scotia, label='Nova Scotia')
plt.plot(years_nunavut, data_nunavut, label='Nunavut')
plt.plot(years_ontario, data_ontario, label='Ontario')
plt.plot(years_prince_edward_island, data_prince_edward_island, label='Prince Edward Island')
plt.plot(years_quebec, data_quebec, label='Quebec')
plt.plot(years_saskatchewan, data_saskatchewan, label='Saskatchewan')
plt.plot(years_yukon, data_yukon, label='Yukon')

plt.xlabel('时间', FontProperties=plot_para())
plt.ylabel('温度(ºC)', FontProperties=plot_para())
plt.title("加拿大各地年平均气温变化图", FontProperties=plot_para())
plt.legend()
# plt.show()
plt.savefig('/Users/thpffcj/Desktop/数据挖掘/数学建模/2019年中国研究生数学建模竞赛赛题/2019年中国研究生数学建模竞赛E题/data/加拿大各地年平均气温变化图.png')


