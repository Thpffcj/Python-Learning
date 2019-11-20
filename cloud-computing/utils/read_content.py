# -*- coding: UTF-8 -*-
# Created by thpffcj on 2019/11/20.

import pymongo

# 连接数据库
client1 = pymongo.MongoClient("101.132.176.87", 27017)

db1 = client1['steam_db']
db1.authenticate("steam", "steam")

table = db1['China.reviews']

data = table.find().limit(1000)
print("数据加载完成...")

for d in data:
    if d["title"] == "不推荐":
        print(d["content"])
