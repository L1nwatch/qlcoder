#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.19 题 16
    1. 删除空格
    2. 回文数判定
    3.
    4.
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


if __name__ == "__main__":
    pass
