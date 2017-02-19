#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.19 题 16
    1. 删除空格
    2. 回文数判定
    3. 二维转一维
    4. 数字字符前移
"""
__author__ = '__L1n__w@tch'


class Solve:
    @staticmethod
    def delete_white_spaces(a_str):
        """
        删除字符串中的所有空格
        参考资料:
            str().replace() 方法
        :param a_str: str(), 比如 "asd af aa z67"
        :return: str(), 删除空格后的字符串, 比如 "asdafaaz67"
        """
        pass

    @staticmethod
    def is_hui_wen(a_str):
        """
        判断字符串是否为回文, 是则返回 True 不是则返回 False
        回文的条件: 顺读和倒读都一样的字符串, 比如
            (1)LEVEL, 顺读是 LEVEL, 倒读还是 LEVEL, 所以是回文
            (2)123312, 顺读是 123312, 倒读是 213321, 123312 != 213321, 所以不是回文
        参考思路:
            (1)复制该字符串, 逆置该字符串, 参考 reversed() 函数, 或者题目2-reverse_str 函数
            (2)遍历每一个字符, 然后依次判断两个字符串的每一个字符是否相等
        :param a_str: str(), 待判断的字符串, 比如 "LEVEL"
        :return: boolean(), True or False, 是回文则返回 True, 否则返回 False
        """
        pass

    @staticmethod
    def matrix_to_list(matrix):
        """
        将 M 行 N 列的二维数组中的数据, 按行的顺序依次放到一维数组中
        :param matrix: list(), 矩阵, 比如 [[33, 33, 33, 33], [44, 44, 44, 44], [55, 55, 55, 55]]
        :return: list(), 列表, 比如 [33, 33, 33, 33, 44, 44, 44, 44, 55, 55, 55, 55]
        """
        pass

    @staticmethod
    def digits_pre_move(a_str):
        """
        将字符串中的所有数字字符顺序前移, 其他字符顺序后移
        参考思路:
            (1)用列表分别存放数字和其他字符
            (2)遍历字符串中每个字符, 如果是数字则放在数字列表中, 否则存在另一个列表中, 参考 str().isdigit() 函数
            (3)将两个列表拼接起来后返回, 参考: "".join(list)
        :param a_str: str(), 比如 "asd123fgh543df"
        :return: str(), 比如 "123543asdfghdf"
        """
        pass


if __name__ == "__main__":
    pass
