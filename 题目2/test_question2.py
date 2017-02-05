#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.05 题目 2
    1. 测试列表排序
    2. 测试字符串逆序
    3. 输出字典 key
"""
import unittest
import string
import random
import io

from collections import OrderedDict
from solve2 import Solve
from contextlib import redirect_stdout

__author__ = '__L1n__w@tch'


class TestSolve(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.test_solve = Solve()

    def test_list_sort(self):
        self.assertEqual([-1, 2, 3], self.test_solve.sort_list([-1, 3, 2]))

        for i in range(10 ** 4):
            test_list = list()
            for j in range(10 ** 2):
                test_list.append(random.randint(-10 ** 4, 10 ** 4))
            right_answer = sorted(test_list)
            my_answer = self.test_solve.sort_list(test_list)
            self.assertEqual(right_answer, my_answer)

    def test_str_reverse(self):
        self.assertEqual("ccbbaa", self.test_solve.reverse_str("aabbcc"))

        for i in range(10 ** 4):
            test_str = str()

            for j in range(10 ** 2):
                test_str += random.choice(string.ascii_letters)
            right_answer = "".join(reversed(test_str))
            my_answer = self.test_solve.reverse_str(test_str)
            self.assertEqual(right_answer, my_answer)

    def test_dict_key_print(self):
        for i in range(10 ** 4):
            test_dict = OrderedDict()
            base_number = 0
            for j in range(10):
                test_dict.setdefault(str(base_number + random.randint(1, 10 ** 2)), None)
            right_answer = self.print_dict_key(test_dict)
            with io.StringIO() as buf, redirect_stdout(buf):
                self.test_solve.print_dict_key(test_dict)
                my_answer = buf.getvalue()
            self.assertEqual(right_answer, my_answer)

    @staticmethod
    def print_dict_key(dict_wait_to_print):
        return ",".join([key for key in dict_wait_to_print]) + ","


if __name__ == "__main__":
    pass
