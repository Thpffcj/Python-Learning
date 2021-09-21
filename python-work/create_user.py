# -*- coding: UTF-8 -*-
# Created by thpffcj on 2021/8/27.

import requests
import json
import datetime
import pandas as pd

authorization = 'Basic MTMxMTUwMTczOTg6aGx5MTEyOTEwMjR0cw=='

headers = {
    'Authorization': authorization,
    'Content-Type': 'application/json',
    'X-Requested-By': 'XMLHttpRequest'
}


# 创建用户
def create_user(username, phone):
    url = "http://172.20.10.6:9000/api/users"

    params = {
        'first_name': str(username)[0],
        'last_name': str(username)[1:],
        'username': str(phone),
        'password': str(phone)[3:],
        'session_timeout_ms': 3600000,
        'roles': [
            'reader'
        ],
        'email': str(phone) + '@qq.com',
        'permissions': []
    }

    # 无返回值
    requests.request("POST", url, headers=headers, data=json.dumps(params))


def user_not_exist(phone):
    url = "http://172.20.10.6:9000/api/users/" + str(phone)
    response = requests.request("GET", url, headers=headers)
    if('Couldn\'t find user' in response.text):
        return True
    else:
        return False


# 根据用户名获取用户id
def get_user_id(phone):
    url = "http://172.20.10.6:9000/api/users/" + str(phone)
    response = requests.request("GET", url, headers=headers)
    print(response.text)
    user_id = json.loads(response.text)['id']
    return user_id


# 创建索引
def create_index(item_id, item_name):
    url = "http://172.20.10.6:9000/api/system/indices/index_sets"

    params = {
        "title": str(item_id) + str(item_name),
        "description": str(item_id) + str(item_name),
        "index_prefix": item_id.lower(),
        "creation_date": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "writable": True,
        "shards": 4,
        "replicas": 0,
        "retention_strategy_class": "org.graylog2.indexer.retention.strategies.DeletionRetentionStrategy",
        "retention_strategy": {
            "max_number_of_indices": "180",
            "type": "org.graylog2.indexer.retention.strategies.DeletionRetentionStrategyConfig"
        },
        "rotation_strategy_class": "org.graylog2.indexer.rotation.strategies.TimeBasedRotationStrategy",
        "rotation_strategy": {
            "type": "org.graylog2.indexer.rotation.strategies.TimeBasedRotationStrategyConfig",
            "rotation_period": "P1D"
        },
        "index_analyzer": "standard",
        "index_optimization_max_num_segments": 1,
        "index_optimization_disabled": False,
        "field_type_refresh_interval": 5000,
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(params))
    print(response.text)
    # 已存在索引
    if 'would conflict with an existing index set' in response.text:
        return None
    else:
        index_set_id = json.loads(response.text)['id']
        return index_set_id


# 创建流
def create_stream(item_id, item_name, index_set_id):
    url = "http://172.20.10.6:9000/api/streams"

    params = {
        'title': str(item_id) + str(item_name),
        'description': str(item_id) + str(item_name),
        'index_set_id': index_set_id,
        'remove_matches_from_default_stream': False
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(params))
    print(response.text)
    stream_id = json.loads(response.text)['stream_id']
    return stream_id


# 分享流给用户
# 缺陷：分享流的用户也有权限，使用admin分享才能替换管理者
def share_stream(stream_id, user_id):
    url = 'http://172.20.10.6:9000/api/authz/shares/entities/grn::::stream:' + str(stream_id)

    payload="{\"selected_grantee_capabilities\":{\"grn::::user:" + str(user_id) + "\":\"own\"}}"

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def start(username, phone, item_id, item_name):
    print(username, phone, item_id, item_name)
    # 项目编号不存在
    if item_id == '无':
        return

    # 用户不存在，则创建用户
    if user_not_exist(phone):
        create_user(username, phone)

    user_id = get_user_id(phone)

    index_set_id = create_index(item_id, item_name)

    if index_set_id != None:
        stream_id = create_stream(item_id, item_name, index_set_id)
        share_stream(stream_id, user_id)


def read_excel():
    file_path = 'data/新的提交单.xlsx'
    data = pd.DataFrame(pd.read_excel(file_path, sheet_name='内网'))

    username = data['负责人']
    phone = data['手机号']
    item_id = data['系统编号']
    item_name = data['系统名称']

    for i in range(0, len(username)):
        start(username[i], phone[i], item_id[i], item_name[i])


if __name__ == '__main__':
    input_type = input("输入操作类型(single/batch)：")

    if input_type == 'single':
        input_username = input("输入用户名：")
        input_phone = input("输入手机号：")
        input_item_id = input("输入项目编号：")
        input_item_name = input("输入项目名称：")

        start(input_username, input_phone, input_item_id, input_item_name)
    elif input_type == 'batch':
        read_excel()
        pass


