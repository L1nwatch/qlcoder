#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.23 题 20
    1. 计算公式
    2. 统计低于平均分的情况
    3. 复制 n 个字符
    4. 找素数
"""
import unittest
import random
import string
import fractions
import gmpy2

from solve20 import Solve

__author__ = '__L1n__w@tch'


class TestSolve(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.test_solve = Solve()

    def test_compute_formula(self):
        test_data = 5
        right_answer = fractions.Fraction(1931, 3600)
        my_answer = self.test_solve.compute_formula(test_data)
        self.assertEqual(right_answer, my_answer)

        for i in range(2 ** 5):
            test_data = random.randint(1, 10 ** 2)
            right_answer = self.compute_formula(test_data)
            my_answer = self.test_solve.compute_formula(test_data)
            self.assertEqual(right_answer, my_answer)

    def test_analysis_low_average(self):
        test_data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
        right_answer = 4, [10, 20, 30, 40]
        my_answer = self.test_solve.analysis_low_average(test_data)
        self.assertEqual(right_answer, my_answer)

        for i in range(10 ** 2):
            test_data = [random.randint(10, 100) for x in range(random.randint(1, 10 ** 2))]
            right_answer = self.analysis_low_average(test_data)
            my_answer = self.test_solve.analysis_low_average(test_data)
            self.assertEqual(right_answer, my_answer)

    def test_combine_n_char(self):
        test_data = 5, "abcdefgh"
        right_answer = "defgh"
        my_answer = self.test_solve.combine_n_char(*test_data)
        self.assertEqual(right_answer, my_answer)

        char_set = string.ascii_letters + string.digits
        for i in range(10 ** 2):
            test_str = "".join([random.choice(char_set) for x in range(random.randint(1, 10 ** 2))])
            test_data = random.randint(0, len(test_str)), test_str
            right_answer = test_str[-test_data[0]:]
            my_answer = self.test_solve.combine_n_char(*test_data)
            self.assertEqual(right_answer, my_answer)

    def test_find_prime_number(self):
        test_data = 5
        right_answer = 7
        my_answer = self.test_solve.find_prime_number(test_data)
        self.assertEqual(right_answer, my_answer)

        for i in range(10 ** 2):
            test_data = random.randint(1, 10 ** 4)
            right_answer = self.find_prime_number(test_data)
            my_answer = self.test_solve.find_prime_number(test_data)
            self.assertEqual(right_answer, my_answer)

    @staticmethod
    def compute_formula(m):
        result = 1
        for i in range(2, m + 1):
            result -= fractions.Fraction(1, i * i)
        return result

    @staticmethod
    def analysis_low_average(test_list):
        average = sum(test_list) / len(test_list)
        low_average = list(filter(lambda x: x < average, test_list))
        return len(low_average), low_average

    @staticmethod
    def find_prime_number(m):
        while True:
            m += 1
            if gmpy2.is_prime(m):
                return m


if __name__ == "__main__":
    pass
