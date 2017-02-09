#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.09 题目 6
    1. 判断是否为公约数
    2. 求公约数个数
    3. 打印矩阵
"""
import gmpy2

__author__ = '__L1n__w@tch'


class Solve:
    @staticmethod
    def is_common_divisor(num1, num2, divisor):
        """
        给正整数 num1, num2 以及数 divisor, 判断 divisor 是不是 num1 和 num2 的公约数
            2 <= num1, num2 <= 10 ** 4
            2 <= divisor <= 10 ** 2
        :param num1: int(), 正整数 1, 比如 33
        :param num2: int(), 正整数 2, 比如 44
        :param divisor: int(), 正整数 3, 比如 11
        :return: boolean(), 判断结果, 比如 11 是 33 和 44 的其中一个公约数, 故判断结果为 True
        """
        pass

    def count_common_divisor(self, num1, num2):
        """
        计算两个数的公共公约数的个数, 比如说 24, 12
        24 的公约数, 有 1, 2, 3, 4, 6, 8, 12, 24
        12 的公约数, 有 1, 2, 3, 4, 6, 12
        于是 24 和 12 的公共公约数为 [1, 2, 3, 4, 6, 12], 于是公共公约数的个数为 6
            2 <= num1, num2 <= 10 ** 4
        :param num1: int(), 正整数 1, 比如 24
        :param num2: int(), 正整数 2, 比如 12
        :return: int(), 公约数个数, 比如 6
        """
        pass

    @staticmethod
    def print_matrix(num):
        """
        打印 num 行 num 列的矩阵, 比如说 num = 3 时:
            1 2 3
            4 5 6
            7 8 9
        num = 4 时:
            1 2 3 4
            5 6 7 8
            9 10 11 12
            13 14 15 16
        注意每个数字后面都有空格, 每一行的末尾都有换行符, 即矩阵用字符串表示, 比如说 3 时: "1 2 3 \n4 5 6 \n7 8 9 \n"
        :param num: int(), 行数和列数, 比如说 3
        :return: None, 直接打印出要求的格式即可
        """
        pass


if __name__ == "__main__":
    pass
