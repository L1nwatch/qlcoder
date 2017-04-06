#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 先试试用 Python3 解决, 不行再切换到 Python2

发现 Python2 的 random 出来的数值和 Python3 的好像不一样, 怪不得半天没过
自己写的方法太慢了, 还是参考讨论区解决吧
"""
import random
import string
import sympy
from hashlib import md5

__author__ = '__L1n__w@tch'

factor_dict = dict()
quest_dict = dict()


def get_line():
    random.seed(10)
    limit = 10000000
    for i in range(limit):
        r = random.randint(1, limit)
        if i % 3 == 0:
            # 神奇了, 这里居然能每次结果都一样
            yield ('p ' + str(r) + ' ' + ''.join(random.sample(string.ascii_letters, 4)) + '\r\n')
        else:
            yield ('v ' + str(r) + '\r\n')


def get_factor(number):
    """
    计算因数
    :param number: int(), 比如 12
    :return: list(), 每个元素都是 number 的因数, 比如 [2, 3, 4, 6]
    """
    result_list = list()
    for i in range(2, number // 2):
        if number % i == 0:
            result_list.append(i)
    return result_list


def get_md5_for_v_operation(line, time_line_list):
    """
    为每个 v 操作计算 md5 值
    :param line: str(), 比如 v 10
    :param time_line_list: list(), 执行该 v 操作的时候当前所有的 p 操作, 比如 ['9586545 cBEK', '7760814 FrPZ']
    :return: str(), 为 md5 值, 比如 "565ba1cd2fc85e4bcbaa7259d2ac677a"
    """
    v_number = int(line.split(" ")[1])
    # 优化一: 如果 v 是质数就直接跳过
    if sympy.isprime(v_number):
        return ""

    factor_list = factor_dict.get(v_number, get_factor(v_number))
    result_list = list()

    for each_p in time_line_list[::-1]:
        p_number, p_content = each_p.split(" ") if " " in each_p else (each_p, " ")
        if p_number in factor_list:
            result_list.append(p_content)

    return md5("-".join(result_list)).hexdigest()


def solve():
    time_line_list = list()
    result_list = list()

    for i, each_line in enumerate(get_line()):
        print("[*] 正在处理第 {} 行, 总共 10000000 行".format(i))
        if each_line.startswith("p"):
            time_line_list.append(each_line.split("p")[1].strip())
        elif each_line.startswith("v"):
            result_list.append(get_md5_for_v_operation(each_line, time_line_list))

    print("[*] 最终结果 {}".format(md5("-".join(result_list)).hexdigest()))


def fast_solve():
    """
    讨论区的思路, 减少解析每一行的时间, 另外不求因数了, 而是直接保存一个字典, 叠加每一个查询的查询结果
    """
    result_list = list()

    # 删去解析每一行的过程, 直接针对性的处理了
    random.seed(10)
    limit = 10000000
    # limit = 10
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


def view(number):
    """
    执行查询操作
    :param number: int(), 表示几号执行了查询操作
    :return: str(), 该查询操作的 md5 值
    """
    output = quest_dict.get(number, "")[:-1]
    quest_dict[number] = ""
    return md5(output.encode("utf8")).hexdigest()


if __name__ == "__main__":
    # solve()   # 需要跑很久
    fast_solve()
