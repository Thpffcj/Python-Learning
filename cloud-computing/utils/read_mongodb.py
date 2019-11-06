# -*- coding: UTF-8 -*-
# Created by thpffcj on 2019/10/30.

import pymongo
import time
import os


# 连接数据库
client = pymongo.MongoClient("101.132.176.87", 27017)

db = client['steam_db']
db.authenticate("steam", "steam")

table = db['China.reviews']

data = table.find().limit(10)
print("数据加载完成...")
# 65175

for i in range(0, 10):
    print(data[i])
