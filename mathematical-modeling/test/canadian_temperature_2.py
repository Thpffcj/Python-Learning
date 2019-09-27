# -*- coding: UTF-8 -*-
# Created by thpffcj on 2019/9/20.

import pandas as pd
import matplotlib.pyplot as plt

data1 = pd.read_csv("卡纳达气候数据/Alberta/CALGARY_1956_1979.csv", skiprows=18)
data2 = pd.read_csv("卡纳达气候数据/Alberta/CALGARY_1881_2012.csv", skiprows=18)
pd.set_option('display.max_columns', 40)
pd.set_option('display.width', 1000)
print(data2)

# time = data1["Date/Time"]
# temp = data1["Mean Temp (°C)"]
#
# plt.plot(time, temp)
# plt.legend()
# plt.show()
