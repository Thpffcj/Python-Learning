# -*- coding: UTF-8 -*-
# Created by thpffcj on 2021/8/29.

import pandas as pd


def write_excel():
    username = []
    phone = []
    item_id = []
    item_name = []

    username.append("刘能")
    phone.append("13312345678")
    item_id.append("S123")
    item_name.append("智能巡检")

    username.append("艾丽丝")
    phone.append("13912345678")
    item_id.append("S124")
    item_name.append("后勤集团")

    dic = {'负责人': username,
           '手机': phone,
           '项目编号': item_id,
           '项目名称': item_name
           }

    df = pd.DataFrame(dic)
    print(df)
    df.to_excel('data/test.xlsx', index=False)


def read_excel():
    file_path = 'data/新的提交单.xlsx'
    i_data = pd.DataFrame(pd.read_excel(file_path, sheet_name='内网'))
    o_data = pd.DataFrame(pd.read_excel(file_path, sheet_name='外网'))

    print(i_data)
    print('----------------')
    print(o_data)



if __name__ == '__main__':
    # write_excel()
    read_excel()
