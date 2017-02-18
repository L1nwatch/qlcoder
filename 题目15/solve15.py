#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.18 题 15
    1. 进制数转换
    2. 找出最长字符串
    3. 判断幻方
    4. 计算公式
"""
__author__ = '__L1n__w@tch'


class Solve:
    @staticmethod
    def number_convert(number, base):
        """
        将十进制正整数转换成 K(2 <= k <= 9)进制数, 并将结果作为返回值返回
        比如 8 转换为 2 进制:
            由于 8 = 1*2^3 + 0*2^2 + 0*2^1 + 0*2^0
            于是 8 转换为 2 进制就是 1000
        参考讲解: http://baike.baidu.com/view/883725.htm?
        参考思路(C 实现代码如下):
                do {
                    result = number % base + result
                    number /= base
                } while (number)
        :param number: int(), 待转换的数, 比如 8
        :param base: int(), 要求转换的进制数, 比如 2
        :return: str(), 转换后的结果, 比如 "1000"
        """
        pass

    @staticmethod
    def find_longest_str(str_list):
        """
        找出最长的一个字符串, 若长度最长的字符串不唯一, 则返回最先找到的那一个
        参考思路:
            1. 设置一个变量, 用于保存最长的那个字符串
            2. 遍历每一个元素, 如果元素的长度大于设置的那个变量, 就把那个变量的值更新为现在遍历到的这个元素
        :param str_list: list(), 每个元素是个字符串, 比如 ["1", "22", "333"]
        :return: str(), 最长的那个字符串, 比如 "333"
        """
        pass

    @staticmethod
    def is_magic_square_odd(a_list):
        """
        判断给定的 n*n(n 为奇数) 的矩阵是否是幻方, 是则返回 True, 不是则返回 False
        幻方的判定条件: 矩阵每行/每列/主对角线及反对角线上元素之和都相等
        比如:
            4 9 2
            3 5 7
            8 1 6
        判断:
            (1) 每行的值, 4 + 9 + 2 == 3 + 5 + 7 == 8 + 1 + 6 == 15, 符合条件
            (2) 每列的值的和都应该为 15, 15 == 4 + 3 + 8 == 9 + 5 + 1 == 2 + 7 + 6
            (3) 主对角线上的和也应该为 15, 15 == 4 + 5 + 6
            (4) 反对角线上的和也应该为 15, 15 == 2 + 5 + 8
            (5) 符合条件, 该矩阵为幻方
        参考思路:
            同上, 依次判断行/列/主对角线/反对角线即可
        :param a_list: list(), 矩阵, 比如 [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
        :return: boolean(), 即 True or False, 是幻方则返回 True
        """
        pass

    @staticmethod
    def compute_formula(m):
        """
        计算公式的值, 公式为:
            t = 2 - 3 - 4 - .... - m
        当 m = 5 时, 公式变为:
            t = 2 - 3 - 4 - 5 = -10
        :param m: int(), m 的值, 比如 5
        :return: int(), 计算的结果, 比如 -10
        """
        pass


if __name__ == "__main__":
    pass
