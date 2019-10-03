# -*- coding: UTF-8 -*-
# Created by thpffcj on 2019/10/2.

import pymongo
import pandas as pd

# 连接数据库
client = pymongo.MongoClient('localhost', 27017)
db = client['test']
table = db['doubanmovies']

data = pd.DataFrame(list(table.find()))

print(data)

