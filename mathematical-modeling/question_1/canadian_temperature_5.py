# -*- coding: UTF-8 -*-
# Created by thpffcj on 2019/9/20.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab as mpl
from matplotlib.font_manager import FontProperties

pd.set_option('display.max_columns', 40)
pd.set_option('display.width', 1000)

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

alberta_max = 0
british_columbia_max = 0
manitoba_max = 0.0
new_brunswick_max = 0.0
newfoundland_labrador_max = 0.0
northwest_TERRITORIES_max = 0.0
nova_scotia_max = 0.0
nunavut_max = 0.0
ontario_max = 0.0
prince_edward_island_max = 0.0
quebec_max = 0.0
saskatchewan_max = 0.0
yukon_max = 0.0

alberta_min = 0
british_columbia_min = 0
manitoba_min = 0.0
new_brunswick_min = 0.0
newfoundland_labrador_min = 0.0
northwest_TERRITORIES_min = 0.0
nova_scotia_min = 0.0
nunavut_min = 0.0
ontario_min = 0.0
prince_edward_island_min = 0.0
quebec_min = 0.0
saskatchewan_min = 0.0
yukon_min = 0.0

interval = 5

flag = 0
# alberta
for i in range(1880, 2019):
    count = alberta[alberta["Year"] == i]["Year"].count()
    if count == 12:
        alberta_max += alberta[alberta["Year"] == i]["Mean Max Temp (°C)"].values.max()
        alberta_min += alberta[alberta["Year"] == i]["Mean Min Temp (°C)"].values.min()

        flag += 1
        if flag == interval:
            alberta_difference = (alberta_max - alberta_min) / interval
            years_alberta.append(i)
            data_alberta.append(alberta_difference)
            flag = 0
            alberta_max = 0
            alberta_min = 0

flag = 0
# british_columbia
for i in range(1937, 2019):
    count = british_columbia[british_columbia["Year"] == i]["Year"].count()
    if count == 12:
        british_columbia_max += british_columbia[british_columbia["Year"] == i]["Mean Max Temp (°C)"].values.max()
        british_columbia_min += british_columbia[british_columbia["Year"] == i]["Mean Min Temp (°C)"].values.min()

        flag += 1
        if flag == interval:
            british_columbia_difference = (british_columbia_max - british_columbia_min) / interval
            years_british_columbia.append(i)
            data_british_columbia.append(british_columbia_difference)
            flag = 0
            british_columbia_difference = 0
            british_columbia_max = 0
            british_columbia_min = 0

flag = 0
# manitoba
for i in range(1938, 2019):
    count = manitoba[manitoba["Year"] == i]["Year"].count()
    if count == 12:
        manitoba_max += manitoba[manitoba["Year"] == i]["Mean Max Temp (°C)"].values.max()
        manitoba_min += manitoba[manitoba["Year"] == i]["Mean Min Temp (°C)"].values.min()

        flag += 1
        if flag == interval:
            manitoba_difference = (manitoba_max - manitoba_min) / interval
            years_manitoba.append(i)
            data_manitoba.append(manitoba_difference)
            flag = 0
            manitoba_max = 0
            manitoba_min = 0

flag = 0
# new_brunswick
for i in range(1871, 2019):
    count = new_brunswick[new_brunswick["Year"] == i]["Year"].count()
    if count == 12:
        new_brunswick_max += new_brunswick[new_brunswick["Year"] == i]["Mean Max Temp (°C)"].values.max()
        new_brunswick_min += new_brunswick[new_brunswick["Year"] == i]["Mean Min Temp (°C)"].values.min()

        flag += 1
        if flag == interval:
            new_brunswick_difference = (new_brunswick_max - new_brunswick_min) / interval
            years_new_brunswick.append(i)
            data_new_brunswick.append(new_brunswick_difference)
            flag = 0
            new_brunswick_max = 0
            new_brunswick_min = 0

flag = 0
# newfoundland_labrador
for i in range(1937, 2019):
    count = newfoundland_labrador[newfoundland_labrador["Year"] == i]["Year"].count()
    if count == 12:
        newfoundland_labrador_max += newfoundland_labrador[newfoundland_labrador["Year"] == i]["Mean Max Temp (°C)"].values.max()
        newfoundland_labrador_min += newfoundland_labrador[newfoundland_labrador["Year"] == i]["Mean Min Temp (°C)"].values.min()

        flag += 1
        if flag == interval:
            newfoundland_labrador_difference = (newfoundland_labrador_max - newfoundland_labrador_min) / interval
            years_newfoundland_labrador.append(i)
            data_newfoundland_labrador.append(newfoundland_labrador_difference)
            flag = 0
            newfoundland_labrador_max = 0
            newfoundland_labrador_min = 0

flag = 0
# northwest_TERRITORIES
for i in range(1895, 2019):
    count = northwest_TERRITORIES[northwest_TERRITORIES["Year"] == i]["Year"].count()
    if count == 12:
        northwest_TERRITORIES_max += northwest_TERRITORIES[northwest_TERRITORIES["Year"] == i][
            "Mean Max Temp (°C)"].values.max()
        northwest_TERRITORIES_min += northwest_TERRITORIES[northwest_TERRITORIES["Year"] == i][
            "Mean Min Temp (°C)"].values.min()

        flag += 1
        if flag == interval:
            northwest_TERRITORIES_difference = (northwest_TERRITORIES_max - northwest_TERRITORIES_min) / interval
            years_northwest_TERRITORIES.append(i)
            data_northwest_TERRITORIES.append(northwest_TERRITORIES_difference)
            flag = 0
            northwest_TERRITORIES_max = 0
            northwest_TERRITORIES_min = 0

flag = 0
# nova_scotia
for i in range(1870, 2019):
    count = nova_scotia[nova_scotia["Year"] == i]["Year"].count()
    if count == 12:
        nova_scotia_max += nova_scotia[nova_scotia["Year"] == i]["Mean Max Temp (°C)"].values.max()
        nova_scotia_min += nova_scotia[nova_scotia["Year"] == i]["Mean Min Temp (°C)"].values.min()

        flag += 1
        if flag == interval:
            nova_scotia_difference = (nova_scotia_max - nova_scotia_min) / interval
            years_nova_scotia.append(i)
            data_nova_scotia.append(nova_scotia_difference)
            flag = 0
            nova_scotia_max = 0
            nova_scotia_min = 0

flag = 0
# nunavut
for i in range(1929, 2019):
    count = nunavut[nunavut["Year"] == i]["Year"].count()
    if count == 12:
        nunavut_max += nunavut[nunavut["Year"] == i]["Mean Max Temp (°C)"].values.max()
        nunavut_min += nunavut[nunavut["Year"] == i]["Mean Min Temp (°C)"].values.min()

        flag += 1
        if flag == interval:
            nunavut_difference = (nunavut_max - nunavut_min) / interval
            years_nunavut.append(i)
            data_nunavut.append(nunavut_difference)
            flag = 0
            nunavut_max = 0
            nunavut_min = 0

flag = 0
# ontario
for i in range(1840, 2019):
    count = ontario[ontario["Year"] == i]["Year"].count()
    if count == 12:
        ontario_max += ontario[ontario["Year"] == i]["Mean Max Temp (°C)"].values.max()
        ontario_min += ontario[ontario["Year"] == i]["Mean Min Temp (°C)"].values.min()

        flag += 1
        if flag == interval:
            ontario_difference = (ontario_max - ontario_min) / interval
            years_ontario.append(i)
            data_ontario.append(ontario_difference)
            flag = 0
            ontario_max = 0
            ontario_min = 0

flag = 0
# prince_edward_island
for i in range(1872, 2019):
    count = prince_edward_island[prince_edward_island["Year"] == i]["Year"].count()
    if count == 12:
        prince_edward_island_max += prince_edward_island[prince_edward_island["Year"] == i]["Mean Max Temp (°C)"].values.max()
        prince_edward_island_min += prince_edward_island[prince_edward_island["Year"] == i]["Mean Min Temp (°C)"].values.min()

        flag += 1
        if flag == interval:
            prince_edward_island_difference = (prince_edward_island_max - prince_edward_island_min) / interval
            years_prince_edward_island.append(i)
            data_prince_edward_island.append(prince_edward_island_difference)
            flag = 0
            prince_edward_island_max = 0
            prince_edward_island_min = 0

flag = 0
# quebec
for i in range(1928, 2019):
    count = quebec[quebec["Year"] == i]["Year"].count()
    if count == 12:
        quebec_max += quebec[quebec["Year"] == i][
            "Mean Max Temp (°C)"].values.max()
        quebec_min += quebec[quebec["Year"] == i][
            "Mean Min Temp (°C)"].values.min()

        flag += 1
        if flag == interval:
            quebec_difference = (quebec_max - quebec_min) / interval
            years_quebec.append(i)
            data_quebec.append(quebec_difference)
            flag = 0
            quebec_max = 0
            quebec_min = 0

flag = 0
# saskatchewan
for i in range(1928, 2019):
    count = saskatchewan[saskatchewan["Year"] == i]["Year"].count()
    if count == 12:
        saskatchewan_max += saskatchewan[saskatchewan["Year"] == i]["Mean Max Temp (°C)"].values.max()
        saskatchewan_min += saskatchewan[saskatchewan["Year"] == i]["Mean Min Temp (°C)"].values.min()

        flag += 1
        if flag == interval:
            saskatchewan_difference = (saskatchewan_max - saskatchewan_min) / interval
            years_saskatchewan.append(i)
            data_saskatchewan.append(saskatchewan_difference)
            flag = 0
            saskatchewan_max = 0
            saskatchewan_min = 0

flag = 0
# yukon
for i in range(1897, 2019):
    count = yukon[yukon["Year"] == i]["Year"].count()
    if count == 12:
        yukon_max += yukon[yukon["Year"] == i]["Mean Max Temp (°C)"].values.max()
        yukon_min += yukon[yukon["Year"] == i]["Mean Min Temp (°C)"].values.min()

        flag += 1
        if flag == interval:
            yukon_difference = (yukon_max - yukon_min) / interval
            years_yukon.append(i)
            data_yukon.append(yukon_difference)
            yukon_max = 0
            yukon_min = 0

plt.plot(years_alberta, data_alberta, label='alberta')
plt.plot(years_british_columbia, data_british_columbia, label='british columbia')
plt.plot(years_manitoba, data_manitoba, label='manitoba')
plt.plot(years_new_brunswick, data_new_brunswick, label='new brunswick')
plt.plot(years_newfoundland_labrador, data_newfoundland_labrador, label='newfoundland labrador')
plt.plot(years_northwest_TERRITORIES, data_northwest_TERRITORIES, label='northwest TERRITORIES')
plt.plot(years_nova_scotia, data_nova_scotia, label='nova_scotia')
plt.plot(years_nunavut, data_nunavut, label='nunavut')
plt.plot(years_ontario, data_ontario, label='ontario')
plt.plot(years_prince_edward_island, data_prince_edward_island, label='prince edward island')
plt.plot(years_quebec, data_quebec, label='quebec')
plt.plot(years_saskatchewan, data_saskatchewan, label='saskatchewan')
plt.plot(years_yukon, data_yukon, label='yukon')

plt.legend()
plt.show()


