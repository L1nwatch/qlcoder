#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.12 居然要学习图论的知识了, NX 啊
"""
import networkx

__author__ = '__L1n__w@tch'


def solve():
    g = networkx.Graph()

    with open("144341511030664.txt", "r") as f:
        for each_line in f:
            # 注意换行符会跟在后面的
            each_line = each_line.strip()
            point0, point1 = each_line.split(" ")
            g.add_edge(point0, point1)

    # 这个题目其实属于图论，只要确定该图（无向图）的被分为几个不连通的子图即为答案
    print(g.number_of_nodes())
    # 需要考虑孤立用户
    length = len(list(networkx.connected_component_subgraphs(g)))
    print("最终答案: {}".format(100000 - g.number_of_nodes() + length))


if __name__ == "__main__":
    solve()
