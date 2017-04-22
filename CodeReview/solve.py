#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 参考讨论区解决一道代码审计的问题

题目链接: http://www.qlcoder.com/task/7692
"""
import gmpy2

__author__ = '__L1n__w@tch'


def solve():
    # 讨论区提到了, 只要把这个公式求解出来就 OK 了: (398*seed) ^ 0xfba802c7  ≡  seed   (mod 2**30)
    module = 2 ** 30
    for i, seed in enumerate(range(0, 10 ** 100)):
        if i % (10 ** 4) == 0:
            print("[*] 目前 seed 为: {}".format(i))

        seed = gmpy2.mpz(seed)
        if ((398 * seed) ^ 0xfba802c7) % module == seed:
            print("[*] 求解得到 seed: {}".format(seed))
            break


if __name__ == "__main__":
    solve()
