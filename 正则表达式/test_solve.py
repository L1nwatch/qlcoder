#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.27 千里码的一道题, 要求写出正则表达式
"""
import unittest
from solve import solve

__author__ = '__L1n__w@tch'


class TestRegex(unittest.TestCase):
    def test_solve(self):
        test_data = "220422197205148440"
        right_answer = False
        my_answer = solve(test_data)
        self.assertEqual(right_answer, my_answer)

        test_data = "654201199306252458"
        right_answer = True
        my_answer = solve(test_data)
        self.assertEqual(right_answer, my_answer)

        test_data = "440407198504173971"
        right_answer = True
        my_answer = solve(test_data)
        self.assertEqual(right_answer, my_answer)

        test_data = "51312419920924287X"
        right_answer = True
        my_answer = solve(test_data)
        self.assertEqual(right_answer, my_answer)


if __name__ == "__main__":
    pass
