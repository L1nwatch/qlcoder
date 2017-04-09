#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 参考时间线 - 1 进行修改

100
4c48c194632769418a0ddb6a71f0ef4a
300
500bba217336a465fb09620b95e2a21e
312 = 313
ec38bc24019ecbfc5434af3bbd0ec224
1000
fd7132177cb7a09d7e6feaf650b8dae8
23031
d6cd4556a9d3bb0fb63c7aa9e1901196
50000
1ac557a8b858afd3fbc3ce3a2f202227
66666
d0d94f7a727dd2c1e3bfdf5d5680695c
100000
61d2c4eefc309870771c1c3a01de72db
"""

import random
import string
from hashlib import md5

__author__ = '__L1n__w@tch'

factor_dict = dict()
quest_dict = dict()
prime_set = set()


def fast_solve():
    """
    讨论区的思路, 减少解析每一行的时间, 另外不求因数了, 而是直接保存一个字典, 叠加每一个查询的查询结果
    """
    result_list = list()

    # 删去解析每一行的过程, 直接针对性的处理了
    random.seed(10)
    limit = 10000000
    # limit = 100
    for i in range(limit):
        print("[*] 正在处理第 {} 行, 总共 {} 行".format(i, limit))
        r = random.randint(1, limit)
        if i % 3 == 0:
            # 神奇了, 这里居然能每次结果都一样
            content = ''.join(random.sample(string.ascii_letters, 4))
            post(r, content, limit)
        else:
            result_list.append(view(r))

    print("[*] 接下来开始计算总的 md5")
    total_md5 = md5("-".join(result_list).encode("utf8")).hexdigest()
    print("[*] 最终计算结果: {}".format(total_md5))


def post(number, content, limit):
    """
    参考讨论区的快速解法
    :param number: int(), 表示几号发布了消息
    :param content: str(), 表示发布了什么内容
    :param limit: int(), 表示总共有多少个人
    :return: None, 直接将发布内容更新到全局 dict 中
    """
    for i in range(2 * number, limit + 1, number):
        quest_dict[i] = "{}-{}".format(content, quest_dict.get(i, ""))

    # 判断 number 是不是素数, 是则通知所有比他小的数
    if number in prime_set:
        for i in range(1, number):
            quest_dict[i] = "{}-{}".format(content, quest_dict.get(i, ""))


def view(number):
    """
    执行查询操作
    :param number: int(), 表示几号执行了查询操作
    :return: str(), 该查询操作的 md5 值
    """
    output = quest_dict.get(number, "")[:-1]
    quest_dict[number] = ""
    return md5(output.encode("utf8")).hexdigest()


def get_prime_set():
    with open("temp_file.txt", "r") as f:
        for each_line in f:
            prime_set.add(int(each_line.strip()))


if __name__ == "__main__":
    get_prime_set()
    fast_solve()
