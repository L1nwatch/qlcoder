#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.11 题 8
    1. 统计单词个数
    2. 计算平均值并返回大于平均值的数
    3. 计算公式的结果
"""

__author__ = '__L1n__w@tch'


class Solve:
    @staticmethod
    def count_words(a_string):
        """
        数一行的单词个数, 比如给出 "Hello World", 共有两个单词, 单词间以空格隔开
        :param a_string: str(), 一行内容, 形式比如 "Word1 Word2 Word3", 不会有特殊字符 !@# 等
        :return: int(), 表示这一行中有多少个单词, 比如 3
        """
        pass

    @staticmethod
    def count_average_and_return_big(a_list):
        """
        计算列表的平均值, 同时求出列表中大于平均值的数
        比如列表 [1, 2, 3]
        则平均值为 (1 + 2 + 3) / 3 = 2, 大于平均值的数有且仅有 [3]
        因此要打印, 注意换行:
            2
            [3]
        :param a_list: list(), 待计算的列表, 比如 [1, 2, 3, 4]
        :return: None, 直接打印题目要求的两个数据, 一个是平均值, 一个是大于平均值的数的列表
        """
        pass

    @staticmethod
    def compute_formula(num):
        """
        计算公式:
            y = 1 / (100 * 100) + 1 / (200 * 200) + 1 / (300 * 300) + ... + 1 / (m * m)
            其中, 10000 >= m >= 100
        小数点后保留 5 位小数, 提示: "{:0.5f}".format(result)
        :param num: int(), 表示 m 的值, 比如 2000
        :return: str(), 公式的计算结果, 比如 "0.00016"
        """
        pass


if __name__ == "__main__":
    pass
