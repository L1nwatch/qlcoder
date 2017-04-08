#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 参考讨论区解决 IP 库这道题
"""

__author__ = '__L1n__w@tch'


def solve():
    with open("ip.data", "r", encoding="ISO-8859-1") as f:
        data = f.read()

    result_dict = {}
    for i in range(0, len(data), 5):
        # 参考讨论区, 计算城市 id
        city_id = ord(data[i + 2]) * 256 + ord(data[i + 3])
        result_dict[city_id] = result_dict.get(city_id, 0) + 256

    # 看讨论区知道的城市 ID 号
    # ['hz'] = 242, ['sh'] = 133, ['bj'] = 29, ['sz'] = 75
    print("{},{},{},{}".format(result_dict[242], result_dict[29], result_dict[133], result_dict[75]))


if __name__ == "__main__":
    solve()
