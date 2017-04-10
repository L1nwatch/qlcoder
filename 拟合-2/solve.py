#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 参考讨论区解决这道题

先按照 拟合-1 的代码试一下再说
"""
import numpy

__author__ = '__L1n__w@tch'


def solve():
    x, y = numpy.loadtxt("145622513871043.txt", unpack=True)
    # 看来这个自由度表示 x 的最大次方啊, 这道题求的是: Y=a*X^5+b*X^4+c*X^3+d*X^2+e*X+f
    print(":".join(map(str, numpy.polyfit(x, y, 5))))  # 5 表示自由度


if __name__ == "__main__":
    solve()
