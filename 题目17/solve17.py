#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.20 题 17
    1. 字符串交叉拼接
    2. 删除字符串指定字符
    3. 矩阵行交换
"""
__author__ = '__L1n__w@tch'


class Solve:
    @staticmethod
    def str_cross_combine(a, b):
        """
        首先把字符串 b 中的字符按逆序存放, 然后将字符串 a 中的字符和字符串 b 中的字符, 按排列的顺序交叉合并到字符串 c 中, 最终返回 c
        过长的剩余字符直接接在 c 的尾部中
        比如:
            字符串 a 为 "abcdefg", 字符串 b 为 "1234"
            (1) 逆置 b, 变成 "4321"
            (2) 依次取出 a 和逆置 b 的字符, 第一次取出 a 中的 "a", 逆置 b 中的 "4", 于是 c 变为 "a4", 第二次 c 变为 "a4b3"
            (3) b 的字符全部取完了, 于是 a 中过长的字符全都放在 c 的尾部
            (4) 最终 c 的结果为 "a4b3c2d1efg"
        参考思路:
            (1) 将 a 以及逆置 b 变为列表
            (2) 利用 while 循环, 当 a 或逆置 b 中还有元素的时候就不结束循环
            (3) 循环内判断 a 是否有元素, 有的话取出最前面一个元素(参考: list.pop(0)), 之后同理判断逆置 b
        :param a: str(), 字符串 a, 比如 "1234"
        :param b: str(), 字符串 b, 比如 "abcdefg"
        :return: str(), 交叉拼接后的结果, 比如 "1g2f3e4dcba"
        """
        pass

    @staticmethod
    def str_delete_odd_ascii(a_str):
        """
        将字符串中下标为偶数同时 ASCII 值为奇数的字符删除
        比如, s 为 "ABCDEFG12345", 其中字符 C 的 ASCII 码值为奇数, 在数组中的下标为偶数, 因此必须删除;
            而字符 1 的 ASCII 码值为奇数, 在数组中的下标为奇数, 因此不应当删除, 其他的以此类推.
        参考思路:
            (1) 新建一个变量用于存放结果
            (2) 遍历字符串的每一个元素, 判断是否为奇数位置, 是则直接插入结果中; 如果是偶数位置, 进一步判断 ASCII 码值, 符合条件才插入
            (3) 遍历的方式, 参考: for i, each_char in enumerate(a_str), 其中 i 用于表示序号, each_char 则是对应的每个字符
        :param a_str: str(), 字符串 s, 比如 "ABCDEFG12345"
        :return: str(), 删除后的结果, 比如 "BDF12345"
        """
        pass

    @staticmethod
    def exchange_matrix_row(k, matrix):
        """
        将矩阵中第 k 行元素与第 1 行元素交换, 比如
            1 2 3
            4 5 6
            7 8 9
            10 11 12
        若 k = 3, 则执行结果为:
            7 8 9
            4 5 6
            1 2 3
            10 11 12
        参考思路:
            本质上是矩阵两个元素的交换, 于是 a,b = b,a 即可
        :param k: int(), 表示第 k 行, 比如 3
        :param matrix:  list(), 矩阵, 比如 [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        :return: list(), 交换后的矩阵, 比如 [[7, 8, 9], [4, 5, 6], [1, 2, 3], [10, 11, 12]]
        """
        pass


if __name__ == "__main__":
    pass
