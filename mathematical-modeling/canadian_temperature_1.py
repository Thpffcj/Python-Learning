# -*- coding: UTF-8 -*-
# Created by thpffcj on 2019/9/20.

import pandas as pd

data = pd.read_csv("Alberta/CALGARY_daily_2012.csv", skiprows=24)
pd.set_option('display.max_columns', 40)
pd.set_option('display.width', 1000)
print(data)

# 返回前n行
# print(data.head(n=5))

'''
Index(['Date/Time', 'Year', 'Month', 'Day', 'Data Quality', 'Max Temp (°C)',
       'Max Temp Flag', 'Min Temp (°C)', 'Min Temp Flag', 'Mean Temp (°C)',
       'Mean Temp Flag', 'Heat Deg Days (°C)', 'Heat Deg Days Flag',
       'Cool Deg Days (°C)', 'Cool Deg Days Flag', 'Total Rain (mm)',
       'Total Rain Flag', 'Total Snow (cm)', 'Total Snow Flag',
       'Total Precip (mm)', 'Total Precip Flag', 'Snow on Grnd (cm)',
       'Snow on Grnd Flag', 'Dir of Max Gust (10s deg)',
       'Dir of Max Gust Flag', 'Spd of Max Gust (km/h)',
       'Spd of Max Gust Flag'],
      dtype='object')
'''
# 返回全部列名
# print(data.columns)
