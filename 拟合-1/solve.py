#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 参考讨论区解决这道题

记得以前用 MATLAB 学过怎么搞定这类题, 但是现在要学习用 Python 咋解决
"""
import numpy

__author__ = '__L1n__w@tch'


def solve():
    x, y = numpy.loadtxt("145613865992313.txt", unpack=True)
    print("-".join(map(str, numpy.polyfit(x, y, 1))))  # 1 表示自由度


if __name__ == "__main__":
    solve()
