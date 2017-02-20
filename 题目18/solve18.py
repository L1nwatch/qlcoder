#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.21 题 18
    1. ASCII 升值排序字符串
    2. 字符串奇数位大小写转换
    3. 矩阵列左移
"""
__author__ = '__L1n__w@tch'


class Solve:
    @staticmethod
    def str_ascii_sort(a_str):
        """
        给定一个字符串, 要求将该字符串中的所有字符按 ASCII 码值升序排序后输出.
        例如, 若给定 "edcba", 则输出 "abcde"
        参考资料:
            sorted() 函数
        :param a_str: str(), 待排序的字符串, 比如 "edcba"
        :return: str(), 排序后的结果, 比如 "abcde"
        """
        pass

    @staticmethod
    def upper_odd_str(a_str):
        """
        将字符串 a_str 中所有下标为奇数位置的字母转换为大写(如果该位置上不是字母, 则不转换)
        参考资料:
            str().isalpha(x): 判断 x 是否为字母
            str().upper(): 将 str 转换为大写
            for i, each_char in enumerate(a_str): 遍历字符串, 其中 i 表示序号, each_char 表示序号对应的字符
        :param a_str: str(), 比如 "abc4Efg"
        :return: str(), 转换后的结果, 比如 "aBc4EFg"
        """
        pass

    @staticmethod
    def matrix_left_move_column(k, matrix):
        """
        将矩阵中的索引值 k 所在列的元素左移到第 1 列, k 列以后的每列元素依次左移, 原来左边的各列依次绕到右边
        例如:
            1 2 3 4 5
            1 2 3 4 5
            1 2 3 4 5
        若 k 为 2, 意味着要将索引值为 2, 也就是第 3 列移动到第 1 列, 原来的第 1 列和第 2 列变为第 4 列和第 5 列, 结果为:
            3 4 5 1 2
            3 4 5 1 2
            3 4 5 1 2
        参考思路:
            本质上是对每行的元素进行移动, 每行的元素中, 比如示例从第 3 个元素开始左移两格
            (1) 遍历每行, 依次对每行进行移动元素的操作
            (2) 左移元素, 其实就是弹出每行列表第 1 个元素, 然后插入到列表最后面去, 也就是先 pop(0) 再 append()
            (3) 循环 k 次, 每次都是左移一个元素, k 次之后就是左移 k 次了
        :param k: int(), 要左移的次数, 比如 2
        :param matrix: list(), 矩阵, 比如 [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
        :return: list(), 左移后的矩阵, 比如 [[3, 4, 5, 1, 2], [3, 4, 5, 1, 2], [3, 4, 5, 1, 2]]
        """
        pass


if __name__ == "__main__":
    pass
