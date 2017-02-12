#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.12 题 9
    1. 计算平均值并返回小于平均值且最接近平均值的数
    2. 计算公式的结果
    3. 矩阵右上半三角元素翻倍
"""
import unittest
import io
import random
import copy

from solve9 import Solve
from contextlib import redirect_stdout

__author__ = '__L1n__w@tch'


class TestSolve(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.test_solve = Solve()

    def test_count_average_and_return_close(self):
        test_data = [46, 30, 32, 40, 6, 17, 45, 15, 48, 26]

        # 检查打印值
        with io.StringIO() as buf, redirect_stdout(buf):
            self.test_solve.count_average_and_return_close(test_data)
            my_answer = buf.getvalue()
        right_answer = "30"
        self.assertEqual(right_answer, my_answer)

        # 检查返回值
        right_answer = 30.5
        my_answer = self.test_solve.count_average_and_return_close(test_data)
        self.assertEqual(right_answer, my_answer)

        for i in range(10 ** 2):
            test_data = list()
            for j in range(10 ** 2):
                test_data.append(random.randint(0, 10 ** 4))

            right_print, right_return = self.count_average_and_return_close(test_data)

            # 检查打印值
            with io.StringIO() as buf, redirect_stdout(buf):
                self.test_solve.count_average_and_return_close(test_data)
                my_answer = buf.getvalue()
            self.assertEqual(right_print, my_answer)

            # 检查返回值
            my_answer = self.test_solve.count_average_and_return_close(test_data)
            self.assertEqual(right_return, my_answer)

    def test_compute_formula(self):
        test_data = 10
        right_answer = "0.61798"
        my_answer = self.test_solve.compute_formula(test_data)
        self.assertEqual(right_answer, my_answer)

        for i in range(10):
            test_data = random.randint(1, 10 ** 2)
            right_answer = self.compute_formula(test_data)
            my_answer = self.test_solve.compute_formula(test_data)
            self.assertEqual(right_answer, my_answer)

    def test_multi_half_matrix(self):
        test_data = (2, [[1, 9, 7], [2, 3, 8], [4, 5, 6]])
        right_answer = [[2, 18, 14], [2, 6, 16], [4, 5, 12]]
        my_answer = self.test_solve.multi_half_matrix(*test_data)
        self.assertEqual(right_answer, my_answer)

        for i in range(10 ** 2):
            test_data = (random.randint(1, 10 ** 2), self.create_random_matrix())
            right_answer = self.multi_half_matrix(*test_data)
            my_answer = self.test_solve.multi_half_matrix(*test_data)
            self.assertEqual(right_answer, my_answer)

    @staticmethod
    def count_average_and_return_close(test_list):
        average = sum(test_list) / len(test_list)
        sorted_list = sorted(test_list)

        max_number = sorted_list[0]

        for i in sorted_list:
            if i >= average:
                break
            else:
                max_number = i

        return str(max_number), average

    @staticmethod
    def compute_formula(num):
        result = 1
        for i in range(num - 1):
            result = 1 / (1 + result)
        return "{:0.5f}".format(result)

    @staticmethod
    def create_random_matrix():
        n = 3
        result_list = list()
        for i in range(n):
            temp_list = list()
            for j in range(n):
                temp_list.append(random.randint(1, 10 ** 3))
            result_list.append(temp_list)

        return result_list

    @staticmethod
    def multi_half_matrix(number, matrix):
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
