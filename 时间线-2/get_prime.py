#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 需要用到素数列表, 写一个来产生素数的吧, set 封装

python3.2 好像无法使用 shelve, 跪了, 先保存到文件然后再用 python3.4 存到 shelve 中吧
话说就算保存成 shelve 但是 pypy3 依旧用不了啊, 还是直接文件吧。。。
"""
import shelve
import gmpy_cffi

__author__ = '__L1n__w@tch'


def get_prime_to_shelve():
    result_file = "prime_set"
    prime_set = set()

    with open("temp_file.txt", "r") as f:
        for each_line in f:
            num = int(each_line.strip())
            print("[*] 正在保存素数 {}".format(num))
            prime_set.add(num)

    with shelve.open(result_file) as f:
        f["prime_set"] = prime_set


def get_prime_to_file(limit):
    with open("temp_file.txt", "w") as f:
        for i in range(0, limit + 1):
            if gmpy_cffi.is_prime(i):
                print("[*] 找到素数 {}, 查找上限为 {}".format(i, limit))
                f.write("{}\n".format(i))


if __name__ == "__main__":
    # max_value = 23031
    max_value = 10000000
    get_prime_to_file(max_value)
    # get_prime_to_shelve()
