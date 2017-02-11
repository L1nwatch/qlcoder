#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.11 题 8
    1. 统计单词个数
    2. 计算平均值并返回大于平均值的数
    3. 计算公式的结果
"""
import unittest
import io
import random

from solve8 import Solve
from contextlib import redirect_stdout

__author__ = '__L1n__w@tch'


class TestSolve(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.test_solve = Solve()

    def test_count_words(self):
        test_data = "Hello World"
        right_answer = 2
        my_answer = self.test_solve.count_words(test_data)
        self.assertEqual(my_answer, right_answer)

        with open("usernames.txt", "r") as f:
            words = f.readlines()

        for i in range(10 ** 4):
            test_data = str()
            right_answer = random.randint(1, 2 ** 8) + 1
            for j in range(right_answer):
                test_data += random.choice(words).strip() + " "
            test_data = test_data.rstrip(" ")
            my_answer = self.test_solve.count_words(test_data)
            self.assertEqual(my_answer, right_answer)

    def test_count_average_and_return_big(self):
        for i in range(10 ** 2):
            test_data = list()
            for j in range(10 ** 2):
                test_data.append(random.randint(0, 10 ** 4))
            right_answer = self.count_average_and_return_big(test_data)
            with io.StringIO() as buf, redirect_stdout(buf):
                self.test_solve.count_average_and_return_big(test_data)
                my_answer = buf.getvalue()
            self.assertEqual(my_answer, right_answer)

    def test_compute_formula(self):
        test_data = 2000
        right_answer = "0.00016"
        my_answer = self.test_solve.compute_formula(test_data)
        self.assertEqual(right_answer, my_answer)

        for i in range(10):
            test_data = random.randint(1, 10 ** 2) * 100
            right_answer = self.compute_formula(test_data)
            my_answer = self.test_solve.compute_formula(test_data)
            self.assertEqual(right_answer, my_answer)

    @staticmethod
    def count_average_and_return_big(a_list):
        average = sum(a_list) / len(a_list)
        big_list = [x for x in a_list if x > average]
        return "{}\n{}\n".format(average, big_list)

    @staticmethod
    def compute_formula(num):
        result = 0
        for i in range(100, num, 100):
            result += 1 / (i ** 2)
        return "{:0.5f}".format(result)


if __name__ == "__main__":
    pass
