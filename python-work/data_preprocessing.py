# -*- coding: UTF-8 -*-
# Created by thpffcj on 2021/8/30.

import pandas as pd

user_to_mobile = {}
system_name_to_system_id = {}

def read_excel():

    i_system_id = []
    i_system_name = []
    i_username = []
    i_phone = []
    i_area = []

    i_dic = {'系统编号': i_system_id,
           '系统名称': i_system_name,
           '负责人': i_username,
           '手机号': i_phone,
           '网络区域': i_area
           }

    o_system_id = []
    o_system_name = []
    o_username = []
    o_phone = []
    o_area = []

    o_dic = {'系统编号': o_system_id,
           '系统名称': o_system_name,
           '负责人': o_username,
           '手机号': o_phone,
           '网络区域': o_area
           }

    approve_file_path = 'data/审批信息.xlsx'
    approve_data = pd.DataFrame(pd.read_excel(approve_file_path, usecols=[9, 17, 18]))

    username = approve_data['发起人姓名']
    system_name = approve_data['系统名称']
    network_area = approve_data['网络区域']


    for i in range(0, len(system_name)):
        if '信息内网' in network_area[i]:
            # 重复系统
            if system_name[i].strip() in i_system_name:
                continue

            if system_name_to_system_id.get(system_name[i].strip()) != None:
                i_system_id.append(system_name_to_system_id.get(system_name[i].strip()))
            else:
                i_system_id.append('')

            i_system_name.append(system_name[i].strip())
            i_username.append(username[i].strip())
            i_phone.append(user_to_mobile.get(username[i].strip()))
            i_area.append('信息内网')
        elif '信息外网' in network_area[i]:
            if system_name[i].strip() in o_system_name:
                continue

            if system_name_to_system_id.get(system_name[i].strip()) != None:
                o_system_id.append(system_name_to_system_id.get(system_name[i].strip()))
            else:
                o_system_id.append('')

            o_system_name.append(system_name[i].strip())
            o_username.append(username[i].strip())
            o_phone.append(user_to_mobile.get(username[i].strip()))
            o_area.append('信息外网')

        df = pd.DataFrame(i_dic)
        df.to_excel('data/内网信息结果.xlsx', index=False)

        df = pd.DataFrame(o_dic)
        df.to_excel('data/外网信息结果.xlsx', index=False)



def init():
    # 读取钉钉用户和手机号
    ding_file_path = 'data/钉钉信息.xlsx'
    ding_data = pd.DataFrame(pd.read_excel(ding_file_path, usecols=[1, 2]))

    username = ding_data['NAME']
    phone = ding_data['MOBILE']
    for i in range(0, len(username)):
        # 重复姓名
        if username[i] in user_to_mobile:
            user_to_mobile[username[i]] = '存在重名'
        else:
            user_to_mobile[username[i]] = phone[i]

    # 读取台账信息
    assets_file_path = 'data/资产模板.xlsx'
    assets_data = pd.DataFrame(pd.read_excel(assets_file_path, sheet_name='编号、名称', usecols=[1, 2]))

    system_id = assets_data['系统编号']
    system_name = assets_data['系统名称']
    for i in range(0, len(system_name)):
        # 重复系统名称
        if system_name[i] in user_to_mobile:
            system_name_to_system_id[system_name[i]] = '存在重复系统名'
        else:
            system_name_to_system_id[system_name[i]] = system_id[i]


if __name__ == '__main__':
    init()
    read_excel()
