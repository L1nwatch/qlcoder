#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.16 题 13
    1. 产生随机列表
    2. 读入矩阵并输出对角线之和
    3. 实现矩阵转置
"""
import unittest
import sys
import io
import random
import copy

from solve13 import Solve

__author__ = '__L1n__w@tch'


class TestSolve(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.test_solve = Solve()

    def test_create_random_list(self):
        for i in range(10):
            answer_list = self.test_solve.create_random_list()
            self.assertTrue(isinstance(answer_list, list), "返回值不是列表")
            answer_list2 = self.test_solve.create_random_list()
            self.assertNotEqual(answer_list, answer_list2, "两次产生的列表相同")

    def test_sum_matrix_cross(self):
        old_standard_in = sys.stdin

        test_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        right_answer = 1 + 5 + 9
        test_input = self.create_matrix_input(test_data)
        sys.stdin = test_input
        my_answer = self.test_solve.sum_matrix_cross(len(test_data))
        self.assertEqual(right_answer, my_answer)

        sys.stdin = old_standard_in

        for i in range(10 ** 2):
            test_data = self.create_random_matrix()
            right_answer = self.sum_matrix_cross(test_data)

            old_standard_in = sys.stdin

            test_input = self.create_matrix_input(test_data)
            sys.stdin = test_input
            my_answer = self.test_solve.sum_matrix_cross(len(test_data))
            self.assertEqual(right_answer, my_answer)

            sys.stdin = old_standard_in

    def test_transpose_matrix(self):
        test_list = [[100, 200, 300], [400, 500, 600], [700, 800, 900]]
        right_answer = [[100, 400, 700], [200, 500, 800], [300, 600, 900]]
        my_answer = self.test_solve.transpose_matrix(test_list)
        self.assertEqual(right_answer, my_answer)

        for i in range(10 ** 2):
            test_list = self.create_random_matrix()
            right_answer = self.transpose_matrix(test_list)
            my_answer = self.test_solve.transpose_matrix(test_list)
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
    def sum_matrix_cross(matrix):
        n = len(matrix)
        result_list = list()

        for i in range(n):
            result_list.append(matrix[i][i])
        return sum(result_list)

    @staticmethod
    def create_matrix_input(matrix):
        result_list = list()

        for each in matrix:
            result_list += each

        return io.StringIO("\n".join([str(x) for x in result_list]))

    @staticmethod
    def transpose_matrix(matrix):
        n = len(matrix)

        result_list = copy.deepcopy(matrix)

        for i in range(n):
            for j in range(n):
                result_list[j][i] = matrix[i][j]

        return result_list

if __name__ == "__main__":
    pass
