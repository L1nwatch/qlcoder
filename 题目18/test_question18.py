#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.21 题 18
    1. ASCII 升值排序字符串
    2. 字符串奇数位大小写转换
    3. 矩阵列左移
"""
import unittest
import random
import string
import copy

from solve18 import Solve

__author__ = '__L1n__w@tch'


class TestSolve(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.test_solve = Solve()

    def test_str_ascii_sort(self):
        test_data = "edcba"
        right_answer = "abcde"
        my_answer = self.test_solve.str_ascii_sort(test_data)
        self.assertEqual(right_answer, my_answer)

        for i in range(10 ** 2):
            test_str = "".join([random.choice(string.ascii_letters) for x in range(random.randint(1, 2 ** 6))])
            right_answer = "".join(sorted(test_str))
            my_answer = self.test_solve.str_ascii_sort(test_str)
            self.assertEqual(right_answer, my_answer)

    def test_upper_odd_str(self):
        test_str = "abc4Efg"
        right_answer = "aBc4EFg"
        my_answer = self.test_solve.upper_odd_str(test_str)
        self.assertEqual(right_answer, my_answer)

        str_dict = string.ascii_letters + string.digits
        for i in range(10 ** 2):
            test_str = "".join([random.choice(str_dict) for x in range(random.randint(1, 10 ** 2))])
            right_answer = self.upper_odd_str(test_str)
            my_answer = self.test_solve.upper_odd_str(test_str)
            self.assertEqual(right_answer, my_answer)

    def test_matrix_left_move_column(self):
        test_data = 2, [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
        right_answer = [[3, 4, 5, 1, 2], [3, 4, 5, 1, 2], [3, 4, 5, 1, 2]]
        my_answer = self.test_solve.matrix_left_move_column(*test_data)
        self.assertEqual(right_answer, my_answer)

        for i in range(10 ** 2):
            test_matrix = self.create_random_matrix()
            k = random.randint(1, 2 ** 5)
            right_answer = self.matrix_left_move_column(k, copy.deepcopy(test_matrix))
            my_answer = self.test_solve.matrix_left_move_column(k, copy.deepcopy(test_matrix))
            self.assertEqual(right_answer, my_answer)

    @staticmethod
    def upper_odd_str(a_str):
        result = str()
        for i, each_char in enumerate(a_str):
            if i % 2 != 0 and each_char.isalpha():
                result += each_char.upper()
            else:
                result += each_char
        return result

    @staticmethod
    def matrix_left_move_column(k, matrix):
        result_list = list()
        for each_row in matrix:
            times = k
            while times > 0:
                each_row.append(each_row.pop(0))
                times -= 1
            result_list.append(each_row)
        return result_list

    @staticmethod
    def create_random_matrix():
        n = random.randint(1, 10)
        m = random.randint(1, 10)

        result_list = list()
        for i in range(n):
            temp_list = list()
            for j in range(m):
                temp_list.append(random.randint(1, 10 ** 2))
            result_list.append(temp_list)

        return result_list


if __name__ == "__main__":
    pass
