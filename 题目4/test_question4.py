#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.07 题目 4
    1. 求解 100 以内的所有素数
    2. 求中位数
    3. 大小写转换
"""
import unittest
import random
import io
import gmpy2
import string

from solve4 import Solve
from contextlib import redirect_stdout

__author__ = '__L1n__w@tch'


class TestSolve(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.test_solve = Solve()
        self.prime_number_list = self.create_prime_number_list()

    def test_get_prime_number(self):
        """
        测试获取指定范围的素数
        """
        test_data = 7
        right_answer = [2, 3, 5, 7]
        my_answer = self.test_solve.get_prime_number(test_data)
        self.assertEqual(right_answer, my_answer)

        for i in range(10 ** 2):
            test_data = random.randint(2, 10 ** 4)
            right_answer = self.get_prime_number(test_data)
            my_answer = self.test_solve.get_prime_number(test_data)
            self.assertEqual(right_answer, my_answer)

    def test_get_middle_number(self):
        test_list = [0, 1, 2, 3, 4]
        right_answer = 2
        my_answer = self.test_solve.get_middle_number(test_list)
        self.assertEqual(right_answer, my_answer)

        test_list = [0, 1, 2, 3]
        right_answer = (1 + 2) / 2
        my_answer = self.test_solve.get_middle_number(test_list)
        self.assertEqual(right_answer, my_answer)

        test_list = [3, 1, 0, 2]
        right_answer = (1 + 2) / 2
        my_answer = self.test_solve.get_middle_number(test_list)
        self.assertEqual(right_answer, my_answer)

        for i in range(10 ** 4):
            test_list = list()
            for j in range(10 ** 2):
                test_list.append(random.randint(0, 10 ** 4))
            right_answer = self.get_middle_number(test_list)
            my_answer = self.test_solve.get_middle_number(test_list)
            self.assertEqual(right_answer, my_answer)

    def test_print_lower_case(self):
        for i in range(10 ** 4):
            test_str = str()
            for j in range(10 ** 2):
                test_str += random.choice(string.ascii_letters + string.digits)
            with io.StringIO() as buf, redirect_stdout(buf):
                self.test_solve.print_lower_case(test_str)
                my_answer = buf.getvalue()
            right_answer = test_str.lower()
            self.assertEqual(my_answer, right_answer)

    @staticmethod
    def return_prime_number(limit=10 ** 5):
        for i in range(1, limit):
            if gmpy2.is_prime(i):
                yield i

    def create_prime_number_list(self):
        prime_number_list = list(self.return_prime_number())
        return prime_number_list

    def get_prime_number(self, number):
        result_list = list()
        for i in self.prime_number_list:
            if i <= number:
                result_list.append(i)
            else:
                break
        return result_list

    @staticmethod
    def get_middle_number(a_list):
        sorted_list = sorted(a_list)
        length = len(sorted_list)
        if length % 2 == 0:
            return (sorted_list[length // 2 - 1] + sorted_list[length // 2]) / 2
        else:
            return sorted_list[length // 2]


if __name__ == "__main__":
    pass
