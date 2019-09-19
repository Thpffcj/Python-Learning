# -*- coding: UTF-8 -*-
# Created by thpffcj on 2019/8/28.

import os


def get_item_info(input_file):
    """
    get item info:[title,genre]
    :param input_file: item info file
    :return: a dict key item_id, value:[title, genre]
    """
    if not os.path.exists(input_file):
        return {}

    item_info = {}
    line_num = 0

    fp = open(input_file)
    for line in fp:
        if line_num == 0:
            line_num += 1
            continue
        item = line.strip().split(",")

        if len(item) < 3:
            continue
        elif len(item) == 3:
            item_id, title, genre = item[0], item[1], item[2]
        # 可能电影标题中包含"，"
        elif len(item) > 3:
            item_id = item[0]
            genre = item[-1]
            title = ",".join(item[1: -1])

        item_info[item_id] = [title, genre]
    fp.close()
    return item_info


def get_ave_score(input_file):
    """
    get item ave rating score
    :param input_file: user rating file
    :return: a dict, key item_id, value:ave_score
    """
    if not os.path.exists(input_file):
        return {}

    line_num = 0
    record_dict = {}
    score_dict = {}

    fp = open(input_file)
    for line in fp:
        if line_num == 0:
            line_num += 1
            continue
        item = line.strip().split(",")

        if len(item) < 4:
            continue

        user_id, item_id, rating = item[0], item[1], float(item[2])
        if item_id not in record_dict:
            record_dict[item_id] = [0, 0]
        record_dict[item_id][0] += 1
        record_dict[item_id][1] += rating
    fp.close()
    for item_id in record_dict:
        score_dict[item_id] = round(record_dict[item_id][1] / record_dict[item_id][0], 3)
    return score_dict


def get_train_data(input_file):
    """
    get train data for LFM model train
    :param input_file: user item rating file
    :return: a list:[(item_id, item_id, label), (user_id1, item_id1, label), ...]
    """
    if not os.path.exists(input_file):
        return {}

    score_dict = get_ave_score(input_file)

    neg_dict = {}
    pos_dict = {}
    train_data = []

    line_num = 0
    score_thr = 4.0
    fp = open(input_file)
    i = 1
    for line in fp:
        if line_num == 0:
            line_num += 1
            continue
        item = line.strip().split(",")

        if len(item) < 4:
            continue

        user_id, item_id, rating = item[0], item[1], float(item[2])
        if user_id not in pos_dict:
            pos_dict[user_id] = []
        if user_id not in neg_dict:
            neg_dict[user_id] = []

        # 如果大于4分，认为用户喜欢这部电影
        if rating >= score_thr:
            # {'1': [('1', 1), ('3', 1)]}
            pos_dict[user_id].append((item_id, 1))
        else:
            # 需要进行负采样
            score = score_dict.get(item_id, 0)
            # {'1': [('70', 3.509), ('223', 3.856)]}
            neg_dict[user_id].append((item_id, score))
    fp.close()
    # 正负样本均衡
    for user_id in pos_dict:
        data_num = min(len(pos_dict[user_id]), len(neg_dict.get(user_id, [])))
        if data_num > 0:
            train_data += [(user_id, pos[0], pos[1]) for pos in pos_dict[user_id]][:data_num]
        else:
            continue

        # 按得分降序排列
        # [('7153', 4.119), ('4993', 4.106), ('134853', 3.814), ('102007', 3.0)]
        sorted_neg_list = sorted(neg_dict[user_id], key=lambda element: element[1], reverse=True)[:data_num]
        train_data += [(user_id, pos[0], 0) for pos in sorted_neg_list]
    return train_data


if __name__ == '__main__':
    # get_item_info("../data/movies.csv")
    # print(get_ave_score("../data/ratings.csv"))
    train_data = get_train_data("../data/ratings.csv")
    # [('337', '1', 1), ('337', '3', 1), ('337', '5', 1), ('337', '6', 1)]
    # print(train_data[:20])
    # print(train_data[train_data[:][0] == '1'])
    print([data for data in train_data if data[0] == '1'])

