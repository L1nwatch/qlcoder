#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.04 针对题目1:
    第2333个能被2或者被3整除的正整数是多少?
"""
import gmpy2

__author__ = '__L1n__w@tch'


class Solve:
    @staticmethod
    def solve():
        # write your answer
        return 0

    @staticmethod
    def is_module(number, module):
        """
        判断一个数是否能被另外一个数整除
        :param number: int(), 待判断的数, 比如 33
        :param module: int(), 除数, 比如 3
        :return: Boolean(), 比如 33 % 3 == 0, 所以返回 True
        """
        # write your code
        return False

    @staticmethod
    def get_count_model_number(counts, model_number):
        """
        求解第 counts 个能被 model_number 整除的正整数
        比如第 4 个能被 3 整除的正整数, 每个数依次为 [3, 6, 9, 12, ...], 所以第 4 个应该是 12
        :param counts: int(), 比如 4
        :param model_number: int(), 比如 3
        :return: int(), 比如 12
        """
        # write your code
        return 0

    @staticmethod
    def get_count_models_number(counts, b=2, c=3):
        """
        求解第 counts 个能被 b 或 c 整除的正整数
        比如第 4 个能被 2 或 3 整除的正整数, 每个数依次为 [2, 3, 4, 6, ...], 所以第 4 个应该是 6
        :param counts: int(), 比如 4
        :param b: int(), 比如 2
        :param c: int(), 比如 3
        :return: int(), 比如 6
        """
        # write your answer
        return 0


if __name__ == "__main__":
    s = Solve()
    s.solve()
