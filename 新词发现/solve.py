#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.03.12 解决一道 qlcoder 的题目, 参考讨论区的思路解决的- -
"""
from collections import Counter

__author__ = '__L1n__w@tch'


def solve():
    with open("santi.txt", "r") as f:
        data = f.read()
    data_length = len(data)

    # 统计
    c = Counter(data)

    word_dict = dict()
    # 筛选一下, 只选出出现次数超过 100 的单词, 同时计算频率
    for each_char, each_times in c.items():
        if each_times >= 100:
            word_dict[each_char] = each_times / data_length

    print("[*] 筛选后的结果为: {}".format(word_dict))

    max_word = ("??", 0)
    # 遍历上一步筛选出来的结果, 两两进行组合, 求出内部凝聚程度最高的单词
    for each_char, each_times in word_dict.items():
        for another_each_char, another_each_times in word_dict.items():
            # 看网上的答案要求两个字符不能一样?
            if each_char != another_each_char:
                current_word = "{}{}".format(each_char, another_each_char)
                current_times = data.count(current_word) / data_length
                current_degree = current_times / (each_times * another_each_times)
                if current_degree > max_word[1]:
                    max_word = (current_word, current_degree)

    print("[*] 求出的内部凝聚程度最高的单词为: {}".format(max_word))


if __name__ == "__main__":
    solve()
