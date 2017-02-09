#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.09 题目 6
    1. 判断是否为公约数
    2. 求公约数个数
    3. 打印矩阵
"""
import unittest
import random
import io
import gmpy2
import string

from solve6 import Solve
from contextlib import redirect_stdout

__author__ = '__L1n__w@tch'


class TestSolve(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.test_solve = Solve()

    def test_is_common_divisor(self):
        test_data = 33, 44, 11
        my_answer = self.test_solve.is_common_divisor(*test_data)
        self.assertTrue(my_answer)

        test_data = 33, 44, 4
        my_answer = self.test_solve.is_common_divisor(*test_data)
        self.assertFalse(my_answer)

        for i in range(10 ** 2):
            test_data = random.randint(2, 10 ** 4), random.randint(2, 10 ** 4), random.randint(2, 10 ** 2)
            right_answer = self.is_common_divisor(*test_data)
            my_answer = self.test_solve.is_common_divisor(*test_data)
            self.assertEqual(right_answer, my_answer)

    def test_count_common_divisor(self):
        test_data = 24, 12
        right_answer = 6  # [1, 2, 3, 4, 6, 12]
        my_answer = self.test_solve.count_common_divisor(*test_data)
        self.assertEqual(my_answer, right_answer)

        for i in range(10 ** 2):
            test_data = random.randint(2, 10 ** 4), random.randint(2, 10 ** 4)
            right_answer = self.count_common_divisor(*test_data)
            my_answer = self.test_solve.count_common_divisor(*test_data)
            self.assertEqual(right_answer, my_answer)

    def test_print_matrix(self):
        test_data = 3
        right_answer = "1 2 3 \n4 5 6 \n7 8 9 \n"
        with io.StringIO() as buf, redirect_stdout(buf):
            self.test_solve.print_matrix(test_data)
            my_answer = buf.getvalue()
        self.assertEqual(right_answer, my_answer)

        for i in range(10):
            test_data = random.randint(1, 10 ** 2)
            right_answer = self.print_matrix(test_data)
            with io.StringIO() as buf, redirect_stdout(buf):
                self.test_solve.print_matrix(test_data)
                my_answer = buf.getvalue()
            self.assertEqual(right_answer, my_answer)

    @staticmethod
    def is_common_divisor(num1, num2, divisor):
        return num1 % divisor == 0 and num2 % divisor == 0

    def count_common_divisor(self, num1, num2):
        result_list = list()
        max_gcd = gmpy2.gcd(num1, num2)

        for i in range(1, max_gcd + 1):
            if self.is_common_divisor(num1, num2, i):
                result_list.append(i)

        return len(result_list)

    @staticmethod
    def print_matrix(num):
        count = 1
        result_list = list()
        for i in range(num):
            for j in range(num):
                result_list.append("{} ".format(count))
                count += 1
            result_list.append("\n")
        return "".join(result_list)


if __name__ == "__main__":
    pass
