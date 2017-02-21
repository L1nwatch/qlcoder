#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.22 题 19
    1. 按规律生成矩阵
    2. 合并整数
    3. 矩阵找数
"""
import unittest
import random

from solve19 import Solve

__author__ = '__L1n__w@tch'


class TestSolve(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.test_solve = Solve()

    def test_create_matrix(self):
        test_data = 2
        right_answer = [[1, 2], [2, 4]]
        my_answer = self.test_solve.create_matrix(test_data)
        self.assertEqual(right_answer, my_answer)

        test_data = 4
        right_answer = [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12], [4, 8, 12, 16]]
        my_answer = self.test_solve.create_matrix(test_data)
        self.assertEqual(right_answer, my_answer)

        for i in range(10):
            test_data = random.randint(1, 10 ** 2)
            right_answer = self.create_matrix(test_data)
            my_answer = self.test_solve.create_matrix(test_data)
            self.assertEqual(right_answer, my_answer)

    def test_unite_int(self):
        test_data = 45, 12
        right_answer = 5241
        my_answer = self.test_solve.unite_int(*test_data)
        self.assertEqual(right_answer, my_answer)

        for i in range(10 ** 2):
            test_data = random.randint(10, 99), random.randint(10, 99)
            right_answer = self.unite_int(*test_data)
            my_answer = self.test_solve.unite_int(*test_data)
            self.assertEqual(right_answer, my_answer)

    def test_find_num_in_matrix(self):
        test_data = [[1, 2, 13, 4], [7, 8, 10, 6], [3, 5, 9, 7]]
        right_answer = 9
        my_answer = self.test_solve.find_num_in_matrix(test_data)
        self.assertEqual(right_answer, my_answer)

        for i in range(10 ** 3):
            test_data = self.create_random_matrix()
            right_answer = self.find_num_in_matrix(test_data)
            my_answer = self.test_solve.find_num_in_matrix(test_data)
            self.assertEqual(right_answer, my_answer)

    @staticmethod
    def create_matrix(m):
        matrix = list()
        for i in range(m):
            column = list()
            for j in range(m):
                column.append((i + 1) * (j + 1))
            matrix.append(column)
        return matrix

    @staticmethod
    def unite_int(a, b):
        str_a = str(a)
        str_b = str(b)
        result = "{}{}{}{}".format(str_a[1], str_b[1], str_a[0], str_b[0])
        return int(result)

    @staticmethod
    def find_num_in_matrix(matrix):
        max_row = list()
        rows, columns = len(matrix), len(matrix[0])

        # 先找出每行最大的那个数, 放在列表中
        for each_row in matrix:
            max_row.append(max(each_row))

        # 再找出每列最小的那个数, 放在列表中
        min_column = list()
        for each_column in range(columns):
            min_column.append(min([matrix[x][each_column] for x in range(rows)]))

        # 按行遍历每个元素, 如果是最大值的那个元素, 再去列表中取出对应位置最小的数, 看是否相等
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == max_row[i] and matrix[i][j] == min_column[j]:
                    return matrix[i][j]

        return None

    @staticmethod
    def create_random_matrix():
        n = 3
        m = 4

        result_list = list()
        for i in range(n):
            temp_list = list()
            for j in range(m):
                temp_list.append(random.randint(1, 10 ** 2))
            result_list.append(temp_list)

        return result_list


if __name__ == "__main__":
    pass
