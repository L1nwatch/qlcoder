#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.10 题目 7
    1. 提取数字的每一位
    2. 科学计数法表示每一位
    3. 2 进制转换
"""

__author__ = '__L1n__w@tch'


class Solve:
    @staticmethod
    def extract_number(number):
        """
        提取一个数字的每一位, 比如说 1024, 每一位分别是 1, 0, 2, 4
        :param number: int(), 待提取的数字, 比如 1024
        :return: list(), 其中每一位用字符串表示, 比如 ["1", "0", "2", "4"]
        """
        pass

    def format_print_number(self, number):
        """
        按指定格式打印十进制数, 比如说 1024
            1024 = 1*10^3 + 0*10^2 + 2*10^1 + 4*10^0
        就意味着 1024 = 1000 + 0 + 20 + 4
        :param number: int(), 待打印的数字, 比如 1024
        :return: str(), 返回格式化打印的结果, 比如 "1*10^3 + 0*10^2 + 2*10^1 + 4*10^0"
        """
        pass

    @staticmethod
    def decimal_to_binary(number):
        """
        将一个十进制转换成二进制, 比如说 0 -> 0, 1 -> 1, 2 -> 10, 3 -> 11, 4 -> 100, 以此类推
        :param number: int(), 待转换的十进制数, 比如说 3
        :return: str(), 转换后的结果, 用字符串表示, 比如说 "11"
        """
        pass


if __name__ == "__main__":
    pass
