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

# 不需要修改的索引id
not_modify_id = [
    '613eaa6bda68d169b1e6e947',
    '613760e3da6d2324a05d459f',
    '613760eada6d2324a05d4668',
    '613760eada6d2324a05d466b',
    '61387312ae86dd7c25426b45'
]


# 修改用户时区
def modify_user_timezone(user_id):
    url = "http://172.20.10.6:9000/api/users/" + str(user_id)

    params = {
        'session_timeout_ms': 3600000,
        'timezone': 'Asia/Shanghai'
    }

    response = requests.request("PUT", url, headers=headers, data=json.dumps(params))
    print(response.text)


# 修改用户角色
def modify_user_role(user_id):
    url = "http://172.20.10.6:9000/api/users/" + str(user_id)

    params = {
        'roles': [
            'reader',
            'User Inspector'
        ],
    }

    response = requests.request("PUT", url, headers=headers, data=json.dumps(params))
    print(response.text)


# 获取用户列表
def get_user_list():
    url = "http://172.20.10.6:9000/api/users"
    response = requests.request("GET", url, headers=headers)
    users = json.loads(response.text)['users']
    for user in users:
        if 'Admin' in user['roles']:
            continue
        modify_user_timezone(user['id'])
        modify_user_role(user['id'])


# 获取流
def get_stream():
    url = "http://172.20.10.6:9000/api/streams"
    response = requests.request("GET", url, headers=headers)
    streams = json.loads(response.text)['streams']
    for stream in streams:
        if stream['disabled']:
            start_stream(stream['id'])


# 启动流
def start_stream(stream_id):
    url = "http://172.20.10.6:9000/api/streams/" + str(stream_id) + "/resume"
    response = requests.request("POST", url, headers=headers)
    print(response.text)


# 修改索引并删除旧索引
def modify_index(new_index_set_id):
    url = "http://172.20.10.6:9000/api/streams"
    response = requests.request("GET", url, headers=headers)
    streams = json.loads(response.text)['streams']
    for stream in streams:
        stream_id = stream['id']
        title = stream['title']
        description = stream['description']
        remove_matches_from_default_stream = stream['remove_matches_from_default_stream']
        old_index_set_id = stream['index_set_id']

        if old_index_set_id not in not_modify_id:
            # 修改索引
            url = "http://172.20.10.6:9000/api/streams/" + str(stream_id)
            params = {
                'title': title,
                'description': description,
                'remove_matches_from_default_stream': remove_matches_from_default_stream,
                'index_set_id': new_index_set_id
            }

            response = requests.request("PUT", url, headers=headers, data=json.dumps(params))
            print(response.text)

            # 删除旧索引
            url = 'http://172.20.10.6:9000/api/system/indices/index_sets/' + str(old_index_set_id) + \
                  '?delete_indices=true'
            response = requests.request("DELETE", url, headers=headers)
            print(response.text)


if __name__ == '__main__':
    get_user_list()
