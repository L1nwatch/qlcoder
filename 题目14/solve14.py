#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.17 题 14
    1. 找出矩阵每列最大值
    2. 交换变量值
    3. 求素数
    4. 构造矩阵
"""
import gmpy2

__author__ = '__L1n__w@tch'


class Solve:
    @staticmethod
    def find_column_max(matrix):
        """
        找出 n*n 矩阵中每列元素中的最大值, 并按顺序存放到一个列表中并返回该列表
        :param matrix: list(), n 维矩阵, 比如 [[1, 2], [3, 4]]
        :return: list(), 每列最大值存放的列表, 比如 [2, 4]
        """
        pass

    @staticmethod
    def exchange_a_b(a, b):
        """
        将两个变量的值进行交换
        :param a: int(), 比如 3
        :param b: int(), 比如 8
        :return: tuple, a 与 b 交换后的结果, 比如 (8, 3)
        """
        pass

    @staticmethod
    def find_prime_number(limit):
        """
        求出小于或等于 limit 的所有素数并存放在一个列表中返回
        参考资料:
            gmpy2.is_prime(x) 函数
        :param limit: int(), 上限值, 比如 7
        :return: list(), 上限值以内的所有素数, 比如 [2, 3, 5, 7]
        """
        pass

    @staticmethod
    def create_matrix(n):
        """
        建立一个 n*n 的矩阵, 矩阵元素的构成规律是: 最外层元素的值全部为 1, 从外向内第 2 层元素的值全部为 2; 第 3 层元素的值全部为 3...
        例如, 若 N = 5, 生成的矩阵为:
            1 1 1 1 1
            1 2 2 2 1
            1 2 3 2 1
            1 2 2 2 1
            1 1 1 1 1
        参考思路:
            1. 创建一个 n*n 的矩阵
            2. 找出下标规律
            3. 按规律对矩阵内的元素赋值
                (1) 假设需要循环 5 次, 循环变量记为 i
                (2) 行赋值: 循环 j 次, 把 [i][i .. (n-i-1)] 以及 [5-i-1][i .. (n-i-1)] 全都赋值为 i + 1
                (3) 列赋值: 循环 j 次, 把 [i .. (n-i-1)][i] 以及 [i .. (n-i-1)][5-i-1] 全都赋值为 i + 1
        :param n: int(), 要求创建的维数, 比如 5
        :return: list(), 创建后的矩阵, 比如
            [[1, 1, 1, 1, 1], [1, 2, 2, 2, 1], [1, 2, 3, 2, 1], [1, 2, 2, 2, 1], [1, 1, 1, 1, 1]]
        """
        pass


if __name__ == "__main__":
    pass
