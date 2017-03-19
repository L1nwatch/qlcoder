#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 要求实现 BWT 算法

参考: http://stackoverflow.com/questions/21297887/performance-issues-in-burrows-wheeler-in-python
"""
from functools import partial
# from hashlib import md5
from Crypto.Hash import MD5

__author__ = '__L1n__w@tch'


def radix_sort(values, key, step=0):
    if len(values) < 2:
        for value in values:
            yield value
        return

    bins = {}
    for value in values:
        bins.setdefault(key(value, step), []).append(value)

    for k in sorted(bins.keys()):
        for r in radix_sort(bins[k], key, step + 1):
            yield r


def bw_key(text, value, step):
    return text[(value + step) % len(text)]


def burroughs_wheeler_custom(text):
    return ''.join(text[i - 1] for i in radix_sort(range(len(text)), partial(bw_key, text)))
    # Notice I've dropped the square brackets; this means I'm passing a generator
    # expression to `join` instead of a list comprehension. In general, this is
    # a little slower, but uses less memory. And the underlying code uses lazy
    # evaluation heavily, so :)


def solve(raw_data):
    after_bwt = burroughs_wheeler_custom(raw_data)
    # return md5(after_bwt.encode("utf8")).hexdigest().lower()
    return MD5.new(after_bwt.encode("utf8")).hexdigest().lower()


if __name__ == "__main__":
    test_data = "^bananabananabanana|"
    right_answer = "bc900e3422bdab3deeb75838e5d09c03"
    my_answer = solve(test_data)
    assert right_answer == my_answer

    with open("144982851178300.txt", "r") as f:
        data = f.read()

    # 将结果保存到文件中
    # result = burroughs_wheeler_custom(data)
    # with open("result.txt", "w") as f:
    #     f.write(result)

    print(solve(data))
