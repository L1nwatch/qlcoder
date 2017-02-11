#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.11 编写访客统计那道题
"""
import re

__author__ = '__L1n__w@tch'


def solve():
    result_set = set()
    id_find = re.compile("[0-9_:]+ (\d+) \S+")

    with open("uv.txt", "r") as f:
        for each_line in f:
            get_id = id_find.findall(each_line)[0]
            result_set.add(get_id)

    print("计算结果为: {}".format(len(result_set)))


if __name__ == "__main__":
    solve()
