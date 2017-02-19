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
import unittest
import random
import string

from solve16 import Solve

__author__ = '__L1n__w@tch'


class TestSolve(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.test_solve = Solve()

    def test_delete_white_spaces(self):
        test_data = "asd af aa z67"
        right_answer = "asdafaaz67"
        my_answer = self.test_solve.delete_white_spaces(test_data)
        self.assertEqual(right_answer, my_answer)

        for i in range(10 ** 2):
            test_str = str()
            for j in range(random.randint(1, 10 ** 4)):
                test_str += random.choice(string.ascii_letters + " ")
            right_answer = test_str.replace(" ", "")
            my_answer = self.test_solve.delete_white_spaces(test_str)
            self.assertEqual(right_answer, my_answer)

    def test_is_hui_wen(self):
        test_data = "LEVEL"
        right_answer = True
        my_answer = self.test_solve.is_hui_wen(test_data)
        self.assertEqual(right_answer, my_answer)

        test_data = "123312"
        right_answer = False
        my_answer = self.test_solve.is_hui_wen(test_data)
        self.assertEqual(right_answer, my_answer)

        for i in range(10 ** 2):
            right_answer = random.choice([True, False])
            test_str = "".join([random.choice(string.ascii_letters) for x in range(10 ** 2)])
            if right_answer:
                test_str += test_str[::-1]
            my_answer = self.test_solve.is_hui_wen(test_str)
            self.assertEqual(right_answer, my_answer)

    def test_matrix_to_list(self):
        test_data = [[33, 33, 33, 33], [44, 44, 44, 44], [55, 55, 55, 55]]
        right_answer = [33, 33, 33, 33, 44, 44, 44, 44, 55, 55, 55, 55]
        my_answer = self.test_solve.matrix_to_list(test_data)
        self.assertEqual(right_answer, my_answer)

        for i in range(10 ** 2):
            test_matrix = self.create_random_matrix()
            right_answer = self.matrix_to_list(test_matrix)
            my_answer = self.test_solve.matrix_to_list(test_matrix)
            self.assertEqual(right_answer, my_answer)

    def test_digits_pre_move(self):
        test_data = "asd123fgh543df"
        right_answer = "123543asdfghdf"
        my_answer = self.test_solve.digits_pre_move(test_data)
        self.assertEqual(right_answer, my_answer)

        for i in range(10 ** 2):
            test_data = "".join([random.choice(string.ascii_letters + string.digits) for x in range(1, 10 ** 4)])
            right_answer = self.digits_pre_move(test_data)
            my_answer = self.test_solve.digits_pre_move(test_data)
            self.assertEqual(right_answer, my_answer)

    @staticmethod
    def digits_pre_move(a_str):
        num_list = list()
        other_list = list()
        for each_char in a_str:
            if each_char.isdigit():
                num_list.append(each_char)
            else:
                other_list.append(each_char)

        return "".join(num_list + other_list)

    @staticmethod
    def matrix_to_list(matrix):
        result = list()
        for each in matrix:
            result += each
        return result

    @staticmethod
    def create_random_matrix():
        n = random.randint(1, 10)
        m = random.randint(1, 10)

        result_list = list()
        for i in range(n):
            temp_list = list()
            for j in range(m):
                temp_list.append(random.randint(1, 10 ** 3))
            result_list.append(temp_list)

        return result_list


if __name__ == "__main__":
    pass
