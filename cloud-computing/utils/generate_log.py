# -*- coding: UTF-8 -*-
# Created by thpffcj on 2019/10/2.

import pymongo
import time
import os

# 连接数据库
client = pymongo.MongoClient("101.132.176.87", 27017)

db = client['steam_db']
db.authenticate("steam", "steam")

table = db['China.games']

data = table.find().limit(10)
print("数据加载完成...")
# os.system("./write_log.sh")


def generate_log(count=10):

    flag = 0
    steam_log = ""
    for game_data in data:
        query_log = "{img_src}\t{game_detail}\t{original_price}\t{price}\t{review_summary}\t{date}\t{name}".format(
            img_src=game_data["img_src"],
            game_detail=str(game_data["game_detail"]).replace("'", "\""),
            original_price=game_data["original_price"],
            price=game_data["price"],
            review_summary=game_data["review_summary"],
            date=game_data["date"],
            name=game_data["name"])

        steam_log = steam_log + query_log + "\n"
        flag = flag + 1

        if flag == count:
            print("写日志...")
            f = open("/Users/thpffcj/Public/local-repository/Python-Learning/cloud-computing/utils/test.log", "w")
            f.write(steam_log)
            flag = 0
            steam_log = ""
            f.close()
            time.sleep(5)

    print("结束...")
    f = open("/Users/thpffcj/Public/local-repository/Python-Learning/cloud-computing/utils/test.log", "w")
    f.write("")
    f.close()


if __name__ == '__main__':
    generate_log()
