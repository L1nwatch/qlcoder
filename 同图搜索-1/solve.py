#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.27 发现用了 imagehash 的几种库 hash 出来的结果都不能完全一样, 但是可以直接相减得到相似度
2017.02.27 解决同图搜索-1
"""
import imagehash
import os
import shelve

try:
    import simplejson as json
except ImportError:
    import json

from PIL import Image

__author__ = '__L1n__w@tch'


def get_picture_hash(dir_name):
    dict1 = dict()
    for i, each_picture in enumerate(os.listdir(dir_name)):
        if each_picture.endswith(".png") or each_picture.endswith(".jpg"):
            picture_hash = imagehash.average_hash(Image.open(os.path.join(dir_name, each_picture)))
            order = os.path.splitext(each_picture)[0]
            dict1[order] = picture_hash
    return dict1


def solve():
    # dir1_path = "2"
    # dir2_path = "ok2"

    # 遍历第一个文件夹的 30 张图片, 保存哈希值到 dict1
    # dict1 = get_picture_hash(dir1_path)

    # 遍历第二个文件夹的 5000 张图片, 保存哈希值到 dict2
    # dict2 = get_picture_hash(dir2_path)

    # 将哈希值 dict1 和哈希值 dict2 保存到 json 文件中, 好吧, 不支持 JSON 序列化, 那就 shelve
    # with shelve.open("result_hash") as f:
    #     f["dict1"] = dict1
    #     f["dict2"] = dict2

    with shelve.open("result_hash") as f:
        dict1 = f["dict1"]
        dict2 = f["dict2"]

    # 遍历每一个 dict2, 与 dict1 的哈希值进行相减, 求出区别度最低的那个, 打印出来
    sum_of_all = 0
    for i in dict1:
        min_hash = None, 9999
        for each_picture_hash in dict2:
            temp_hash = dict2[each_picture_hash] - dict1[i]
            if temp_hash < min_hash[1]:
                min_hash = each_picture_hash, temp_hash
        print("与第 {} 张图片最相似的是: {}".format(i, min_hash[0]))
        sum_of_all += int(min_hash[0])
    print("最终总和为: {}".format(sum_of_all))


if __name__ == "__main__":
    solve()
