#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.23 题 20
    1. 计算公式
    2. 统计低于平均分的情况
    3. 复制 n 个字符
    4. 找素数
"""
import fractions
import gmpy2

__author__ = '__L1n__w@tch'


class Solve:
    @staticmethod
    def compute_formula(m):
        """
        给定 m 值, 求出 t 值
        计算公式:
            t = 1 - 1/(2*2) - 1/(3*3) - ... - 1/(m*m)
        最后结果用分数表示
        参考资料:
            fractions.Fraction(分子, 分母)
            比如 a = fractions.Fraction(1, 2), b = fractions.Fraction(1, 3)
            则 a + b = 5/6 = fractions.Fraction(5, 6)
        :param m: int(), 比如 5
        :return: fractions.Fraction(), 分数表示, 比如 fractions.Fraction(1931, 3600)
        """
        pass

    @staticmethod
    def analysis_low_average(test_list):
        """
        给定一个列表, 将低于平均分的人数作为函数值返回, 将低于平均分的分数放在列表中返回
        参考资料:
            sum(list) 可以对列表中所有元素进行求和操作
        :param test_list: list(), 比如 [10, 20, 30, 40, 50, 60, 70, 80, 90]
        :return: tuple, (int(), list()), 前者是低于平均分的人数, 后者是低于平均分的分数, 比如 (4, [10, 20, 30, 40])
        """
        pass

    @staticmethod
    def combine_n_char(n, a_str):
        """
        给定一个字符串 s, 要求将字符串 s 中最右边 n 个字符作为返回值返回
        比如 s = "abcdefgh", 最右边 5 个字符即为 "defgh"
        参考资料:
            s[1:3] 表示 s 的第 1 个字符到第 3 个字符, 比如 "bcd"
            s[1:] 表示 s 的第 1 个字符到最后一个字符, 比如 "bcdefgh"
            s[1:-1] 表示 s 的第 1 个字符到倒数第 1 个字符, 比如 "bcdefg"
        :param n: int(), 比如 5
        :param a_str: str(), 比如 "abcdefgh"
        :return: str(), 比如 "defgh"
        """
        pass

    @staticmethod
    def find_prime_number(m):
        """
        找出一个大于给定整数 m 且紧随 m 的素数, 作为函数值返回
        比如 5, 大于 5 且最接近 5 的素数是 7
        参考思路:
            从 5 开始依次加 1, 然后判断每个数是不是素数, 参考: gmpy2.is_prime(x) 函数
        :param m: int(), 比如 5
        :return: int(), 比如 7
        """
        pass


if __name__ == "__main__":
    pass
