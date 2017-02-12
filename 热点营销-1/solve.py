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

    with open("144047638844506.txt", "r") as f:
        for each_line in f:
            point0, point1 = each_line.split(" ")
            g.add_edge(point0, point1)

    # 这个题目其实属于图论，只要确定该图（无向图）的被分为几个不连通的子图即为答案
    print("最终答案: {}".format(len(list(networkx.connected_component_subgraphs(g)))))


if __name__ == "__main__":
    solve()
