#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.12 题 9
    1. 计算平均值并返回小于平均值且最接近平均值的数
    2. 计算公式的结果
    3. 矩阵右上半三角元素翻倍
"""
import copy

__author__ = '__L1n__w@tch'


class Solve:
    @staticmethod
    def count_average_and_return_close(test_list):
        """
        计算平均值, 将平均值作为返回值返回
        找出小于平均值且最接近平均值的一个数, 思路是: 先排序, 然后依次遍历每个元素, >= 平均值之前的那个元素即为答案
        具体例子:
            [46, 30, 32, 40, 6, 17, 45, 15, 48, 26]
            计算平均值, 得到 30.5 返回该值, float() 或 int() 类型即可
            找出小于且最接近平均值的那个数, 排序后知道平均值中间的结果为: [..., 30, 32,...]
                32 是第一个大于平均值的数, 所以 32 之前的 30 即为正确答案, 打印 "30", 注意不带换行符
        :param test_list: list(), 比如 [46, 30, 32, 40, 6, 17, 45, 15, 48, 26]
        :return: int() or float(), 平均值, 比如 30.5 ; 注意还要求打印出小于且最接近平均值的数
        """
        pass

    @staticmethod
    def compute_formula(num):
        """
        计算公式:
            A1 = 1, A2 = 1 / (1 + A1), A3 = 1 / (1 + A2), ... An = 1 / (1 + A(n - 1)), 最终的 An 即为正确答案
            其中, 100 >=n >= 1
        小数点后保留 5 位小数, 提示: "{:0.5f}".format(result)
        :param num: int(), 表示 m 的值, 比如 10
        :return: str(), 公式的计算结果, 比如 "0.61798"
        """
        pass

    @staticmethod
    def multi_half_matrix(number, matrix):
        """
        matrix 是一个 N*N 的二维数组, 这里固定 N=3, 比如:
            [
                [1, 9, 7],
                [2, 3, 8],
                [4, 5, 6],
            ]
        现在要求对角线以及对角线右上角的每一个元素都乘以 number, 并将计算后的结果返回, 假设 number = 2, 则计算结果为:
            [
                [2, 18, 14],
                [2, 6, 16],
                [4, 5, 12],
            ]
        所以返回 [[2, 18, 14], [2, 6, 16], [4, 5, 12]] 即为正确答案
        :param number: int(), 要乘以的倍数, 此处 1 <= number <= 10 ** 2, 比如 2
        :param matrix: list(), 二维数组, 固定为 3*3 的矩阵, 比如 [[1, 9, 7], [2, 3, 8], [4, 5, 6]]
        :return: list(), 翻倍后的矩阵, 比如 [[2, 18, 14], [2, 6, 16], [4, 5, 12]]
        """
        # 复制矩阵
        result_list = copy.deepcopy(matrix)
        # 计算矩阵的维数
        length = len(matrix)
        # 遍历每一个右上角元素
        for i in range(length):
            for j in range(i, length):
                # 通过下标找出右上半角元素, 乘以 number
                result_list[i][j] *= number
        return result_list


if __name__ == "__main__":
    pass
