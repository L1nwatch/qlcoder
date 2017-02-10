#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.10 题目 7
    1. 提取数字的每一位
    2. 科学计数法表示每一位
    3. 2 进制转换
"""
import unittest
import random

from solve7 import Solve

__author__ = '__L1n__w@tch'


class TestSolve(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.test_solve = Solve()

    def test_extract_number(self):
        test_data = 1024
        right_answer = ["1", "0", "2", "4"]
        my_answer = self.test_solve.extract_number(test_data)
        self.assertEqual(right_answer, my_answer)

        for i in range(10 ** 4):
            test_data = random.randint(0, 10 ** 9)
            my_answer = self.test_solve.extract_number(test_data)
            right_answer = self.extract_number(test_data)
            self.assertEqual(my_answer, right_answer)

    def test_format_print_number(self):
        test_data = 1024
        right_answer = "1*10^3 + 0*10^2 + 2*10^1 + 4*10^0"
        my_answer = self.test_solve.format_print_number(test_data)
        self.assertEqual(right_answer, my_answer)

        for i in range(10 ** 4):
            test_data = random.randint(1, 10 ** 9)
            right_answer = self.format_print_number(test_data)
            my_answer = self.test_solve.format_print_number(test_data)
            self.assertEqual(right_answer, my_answer)

    def test_decimal_to_binary(self):
        test_data = 3
        right_answer = "11"
        my_answer = self.test_solve.decimal_to_binary(test_data)
        self.assertEqual(right_answer, my_answer)

        for i in range(10 ** 4):
            test_data = random.randint(0, 10 ** 6)
            right_answer = bin(test_data)[2:]
            my_answer = self.test_solve.decimal_to_binary(test_data)
            self.assertEqual(right_answer, my_answer)

    @staticmethod
    def extract_number(number):
        return list(str(number))

    def format_print_number(self, number):
        each_number = self.extract_number(number)
        length = len(each_number)
        answer = str()
        for each in each_number:
            if answer != "":
                answer += " + "
            answer += "{}*10^{}".format(each, length - 1)
            length -= 1
        return answer


if __name__ == "__main__":
    pass
