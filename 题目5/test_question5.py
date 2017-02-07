#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.08 题目 5
    1. 最大公约数
    2. 最小公倍数
    3. 大小写转换
"""
import unittest
import random
import io
import gmpy2
import string

from solve5 import Solve
from contextlib import redirect_stdout

__author__ = '__L1n__w@tch'


class TestSolve(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.test_solve = Solve()

    def test_get_gcd(self):
        test_data = 33, 44
        right_answer = 11
        my_answer = self.test_solve.get_gcd(*test_data)
        self.assertEqual(right_answer, my_answer)

        for i in range(10 ** 4):
            test_data = random.randint(1, 10 ** 4), random.randint(1, 10 ** 4)
            right_answer = gmpy2.gcd(*test_data)
            my_answer = self.test_solve.get_gcd(*test_data)
            self.assertEqual(right_answer, my_answer)

    def test_get_lcm(self):
        test_data = 3, 4
        right_answer = 12
        my_answer = self.test_solve.get_lcm(*test_data)
        self.assertEqual(right_answer, my_answer)

        for i in range(10 ** 4):
            test_data = random.randint(1, 10 ** 4), random.randint(1, 10 ** 4)
            right_answer = gmpy2.lcm(*test_data)
            my_answer = self.test_solve.get_lcm(*test_data)
            self.assertEqual(right_answer, my_answer)

    def test_print_upper_case(self):
        for i in range(10 ** 4):
            test_str = str()
            for j in range(10 ** 2):
                test_str += random.choice(string.ascii_letters + string.digits)
            with io.StringIO() as buf, redirect_stdout(buf):
                self.test_solve.print_upper_case(test_str)
                my_answer = buf.getvalue()
            right_answer = test_str.upper()
            self.assertEqual(my_answer, right_answer)


if __name__ == "__main__":
    pass
