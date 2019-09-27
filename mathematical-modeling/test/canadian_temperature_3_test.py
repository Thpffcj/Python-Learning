# -*- coding: UTF-8 -*-
# Created by thpffcj on 2019/9/20.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

print(alberta)
print(british_columbia)
print(manitoba)
print(new_brunswick)
print(newfoundland_labrador)
print(northwest_TERRITORIES)
print(nova_scotia)
print(nunavut)
print(ontario)
print(prince_edward_island)
print(quebec)
print(saskatchewan)
print(yukon)
