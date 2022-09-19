# -*- coding: utf-8 -*-
# @Author : 3zz
# @Time   : 2019-07-06 00:41
# @File   : reader.py

import os


def get_user_click(rating_file):
    """
    get user click list
    :param rating_file: input file
    :return: dict,key: useid, value:[itemid1, itemid2...]
    """
    if not os.path.exists(rating_file):
        return {},{}
    fp = open(rating_file)#读取的文件信息保存在fp中
    num = 0
    user_click = {}
    user_click_time = {}
    for line in fp:
        if num == 0:
            num += 1
            continue
        item = line.strip().split(',')
        if len(item) < 4:
            continue
        [userid, itemid, rating, timestamp] = item#对fp中的每一个line进行分解，分为四个变量
        if userid + '_' + itemid not in user_click_time:#"user_click_time"这个字典中键为"userid_itemid", 值为当前user对当前item的点击次数
            user_click_time[userid + "_" + itemid] = int(timestamp)
        if float(rating) < 3.0:#评分小于3.0的直接跳过，到下一行
            continue
        if userid not in user_click:#这个字典的键为userid, 值为数组[itemid], 表示当前id的用户点击过哪些item
            user_click[userid] = []
        user_click[userid].append(itemid)
    fp.close()
    return user_click, user_click_time


def get_item_info(item_file):#获取item的信息
    """
    get item info[title,genres]
    :param item_file: input iteminfo file
    :return: a dict, key itemid, value[item, genres]
    """
    if not os.path.exists(item_file):
        return {}#返回一个空字典
    num = 0
    item_info = {}
    fp = open(item_file)
    for line in fp:
        if num == 0:
            num += 1
            continue
        item = line.strip().split(',')
        if len(item) < 3:#长度小于3的line跳过，排除了数据不全的情况
            continue
        if len(item) == 3:
            [itemid, title, genres] = item
        elif len(item) > 3:#长度大于3的line可能是因为item的名字中含有特殊符号，在这里使其得以保留
            itemid = item[0]
            genres = item[-1]
            title = ",".join(item[1:-1])
        if itemid not in item_info:
            item_info[itemid] = [title, genres]
    fp.close()
    return item_info#返回一个字典，键为"itemid", 值为[title, genres](名字和类型)


if __name__ == "__main__":
    user_click, user_click_time = get_user_click("../data/ratings.txt")
    # print(len(user_click))
    # print(user_click)
    # print(user_click_time)
    item_info = get_item_info("../data/movies.txt")
    print(item_info["5"])
