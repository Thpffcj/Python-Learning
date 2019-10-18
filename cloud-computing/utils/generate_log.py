# -*- coding: UTF-8 -*-
# Created by thpffcj on 2019/10/2.

import pymongo

# 连接数据库
client = pymongo.MongoClient('localhost', 27017)
db = client['test']
table = db['doubanmovies']

# 读取数据
data = list(table.find())

log = ""
for d in data:
    star = d['star']
    bd = d['title']
    quote = d['quote']
    title = d['title']

    query_log = "{star}\t{bd}\t{quote}\t{title}\n".format(
        star=star, bd=bd, quote=quote, title=title)

    log = log + query_log

print(log)



