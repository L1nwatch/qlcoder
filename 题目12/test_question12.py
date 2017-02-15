#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.15 题 12
    1. 字符串面值的整数求和
    2. 统计大小写字母格式
    3. 保留小数位数
"""
import unittest
import io
import random
import string
import gmpy2

from solve12 import Solve
from contextlib import redirect_stdout

__author__ = '__L1n__w@tch'


class TestSolve(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.test_solve = Solve()

    def test_compute_int_add(self):
        test_data = "32486", "12345"
        right_answer = 44831
        my_answer = self.test_solve.compute_int_add(*test_data)
        self.assertEqual(right_answer, my_answer)

        for i in range(10 ** 4):
            test_data = str(random.randint(-10 ** 8, 10 ** 8)), str(random.randint(-10 ** 8, 10 ** 8))
            right_answer = self.compute_int_add(*test_data)
            my_answer = self.test_solve.compute_int_add(*test_data)
            self.assertEqual(right_answer, my_answer)

    def test_count_upper_and_lower(self):
        test_data = "AAaaBBbb123CCcccd"
        right_answer = "upper=6,lower=8\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            self.test_solve.count_upper_and_lower(test_data)
            my_answer = buf.getvalue()
        self.assertEqual(right_answer, my_answer)

        for i in range(10 ** 2):
            test_data = str()
            length = random.randint(1, 10 ** 3)
            for j in range(length):
                test_data += random.choice(string.ascii_letters + string.digits)
            right_answer = self.count_upper_and_lower(test_data)

            with io.StringIO() as buf, redirect_stdout(buf):
                self.test_solve.count_upper_and_lower(test_data)
                my_answer = buf.getvalue()
            self.assertEqual(right_answer, my_answer)

    def test_save_two_decimal_places(self):
        test_data = 1234.567
        right_answer = "1234.57"
        my_answer = self.test_solve.save_two_decimal_places(test_data)
        self.assertEqual(right_answer, my_answer)

        for i in range(10 ** 4):
            test_data = 1234 + random.random()
            right_answer = "{:0.2f}".format(test_data)
            my_answer = self.test_solve.save_two_decimal_places(test_data)
            self.assertEqual(right_answer, my_answer)

    @staticmethod
    def compute_int_add(str1, str2):
        num1, num2 = gmpy2.mpz(str1), gmpy2.mpz(str2)
        return num1 + num2

    @staticmethod
    def count_upper_and_lower(a_str):
        upper_number = 0
        lower_number = 0
        for each_char in a_str:
            if each_char.islower():
                lower_number += 1
            elif each_char.isupper():
                upper_number += 1
        return "upper={},lower={}\n".format(upper_number, lower_number)


if __name__ == "__main__":
    pass
