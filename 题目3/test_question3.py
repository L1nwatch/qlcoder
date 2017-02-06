#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.06 题目 3
    1. 输出字符串奇数位置的字符串
    2. 判断一个数是不是素数
    3. 求矩形面积和周长
"""
import unittest
import random
import io
import gmpy2
import string

from solve3 import Solve
from contextlib import redirect_stdout

__author__ = '__L1n__w@tch'


class TestSolve(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.test_solve = Solve()

    def test_print_odd_char(self):
        for i in range(10 ** 4):
            test_str = str()
            for j in range(10 ** 2):
                test_str += random.choice(string.ascii_letters + string.digits)
            right_answer = "".join(test_str[::2])
            with io.StringIO() as buf, redirect_stdout(buf):
                self.test_solve.print_odd_char(test_str)
                my_answer = buf.getvalue()
            self.assertEqual(right_answer, my_answer)

    def test_is_prime_number(self):
        self.assertEqual(self.test_solve.is_prime_number(7), True)

        for i in range(10 ** 2):
            test_number = random.randint(2, 10 ** 6)
            right_answer = gmpy2.is_prime(test_number)
            my_answer = self.test_solve.is_prime_number(test_number)
            self.assertEqual(right_answer, my_answer)

    def test_calculate_rectangle_area_perimeter(self):
        length, width = 3, 4
        right_answer = 12, 14
        self.assertEqual(right_answer, self.test_solve.calculate_rectangle_area_perimeter(length, width))

        for i in range(10 ** 4):
            test_length, test_width = gmpy2.mpz(random.randint(1, 10 ** 4)), gmpy2.mpz(random.randint(1, 10 ** 4))
            right_answer = test_length * test_width, (test_length + test_width) * 2
            my_answer = self.test_solve.calculate_rectangle_area_perimeter(test_length, test_width)
            self.assertEqual(right_answer, my_answer)


if __name__ == "__main__":
    pass
