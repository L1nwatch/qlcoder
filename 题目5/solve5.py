#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.08 题目 5
    1. 最大公约数
    2. 最小公倍数
    3. 大小写转换
"""

__author__ = '__L1n__w@tch'


class Solve:
    def get_gcd(self, x, y):
        """
        计算 x 和 y 的最大公约数, 1 <= x, y <= 10 ** 4
        :param x: int(), 比如 33
        :param y: int(), 比如 44
        :return: int(), 计算得到的最大公约数, 比如 11
        """
        pass

    def get_lcm(self, x, y):
        """
        计算 x 和 y 的最小公倍数, 1 <= x, y <= 10 ** 4
        公式参考:
            x 与 y 的最小公倍数 = (x * y) // (x 与 y 的最大公约数)
        :param x: int(), 比如 3
        :param y: int(), 比如 4
        :return: int(), 计算得到的最小公倍数, 比如 12
        """
        pass

    @staticmethod
    def print_upper_case(a_str):
        """
        将字符串中的大写字母转换为小写字母并打印出来
        :param a_str: str(), 比如 "aAb", 要求打印 "aab"
        :return: None, 打印转换小写后的字符串
        """
        pass


if __name__ == "__main__":
    pass
