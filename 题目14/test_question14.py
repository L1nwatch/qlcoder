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
import unittest
import gmpy2
import random

from solve14 import Solve

__author__ = '__L1n__w@tch'


class TestSolve(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.test_solve = Solve()

    def test_find_column_max(self):
        for i in range(10 ** 2):
            test_matrix = self.create_random_matrix()
            right_answer = [max(x) for x in test_matrix]
            my_answer = self.test_solve.find_column_max(test_matrix)
            self.assertEqual(right_answer, my_answer)

    def test_exchange_a_b(self):
        test_data = 3, 8
        right_answer = 8, 3
        my_answer = self.test_solve.exchange_a_b(*test_data)
        self.assertEqual(right_answer, my_answer)

        for i in range(10 ** 2):
            test_data = random.randint(-10 ** 8, 10 ** 8), random.randint(-10 ** 8, 10 ** 8)
            right_answer = (test_data[1], test_data[0])
            my_answer = self.test_solve.exchange_a_b(*test_data)
            self.assertEqual(right_answer, my_answer)

    def test_find_prime_number(self):
        for i in range(10):
            test_data = random.randint(2, 10 ** 5)
            right_answer = [x for x in range(test_data + 1) if gmpy2.is_prime(x)]
            my_answer = self.test_solve.find_prime_number(test_data)
            self.assertEqual(right_answer, my_answer)

    def test_create_matrix(self):
        test_data = 5
        right_answer = [[1, 1, 1, 1, 1], [1, 2, 2, 2, 1], [1, 2, 3, 2, 1], [1, 2, 2, 2, 1], [1, 1, 1, 1, 1]]
        my_answer = self.test_solve.create_matrix(test_data)
        self.assertEqual(right_answer, my_answer)

        for i in range(20):
            test_data = i + 1
            right_answer = self.create_matrix(test_data)
            my_answer = self.test_solve.create_matrix(test_data)
            self.assertEqual(right_answer, my_answer)

    @staticmethod
    def create_random_matrix():
        n = random.randint(1, 10)
        result_list = list()
        for i in range(n):
            temp_list = list()
            for j in range(n):
                temp_list.append(random.randint(1, 10 ** 3))
            result_list.append(temp_list)

        return result_list

    @staticmethod
    def create_matrix(n):
        # 创建一个矩阵
        matrix = [[j for j in range(n)] for i in range(n)]

        # 按规律赋值
        for i in range(n):
            # 第一行和最后一行赋值
            for j in range(i, n - i):
                matrix[i][j] = i + 1
                matrix[n - i - 1][j] = i + 1
            # 第一列和最后一列赋值
            for j in range(i, n - i):
                matrix[j][i] = i + 1
                matrix[j][n - i - 1] = i + 1

        return matrix


if __name__ == "__main__":
    pass
