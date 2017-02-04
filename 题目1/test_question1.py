#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.04 针对题目1:
    第2333个能被2或者被3整除的正整数是多少?

分为几个测试方法:
    1. 测试求模是否正确
    2. 测试获取指定数量的被整除数是否正确(包括单个模数, 多个模数的情况)
    3. 测试是否正确求解题目了
"""
import gmpy2
import unittest
import random
from solve1 import Solve

__author__ = '__L1n__w@tch'


class TestSolve(unittest.TestCase):
    def setUp(self):
        self.test_solve = Solve()

    def test_is_model_number(self):
        """
        给定一个数, 给定模数, 判断是否能够整除
        """
        for i in range(10000):
            test_number = gmpy2.mpz(random.randint(-10 ** 100, 10 ** 100))
            model_number = random.randint(1, 10 ** 2)
            if model_number > test_number:
                continue
            else:
                right_answer = test_number % model_number == 0
                my_answer = self.test_solve.is_module(test_number, model_number)
                self.assertEqual(my_answer, right_answer,
                                 "[-] 数 {} 能否被 {} 整除?正确答案是: {}".format(test_number, model_number, right_answer))

    def test_get_count_model_number(self):
        """
        给定一个数 n, 给定模数 m, 求出第 n 个能够被 m 整除的 正整数
        """
        for i in range(10 ** 2):
            test_number = random.randint(1, 10 ** 3)
            model_number = random.randint(2, 23)
            right_answer = self.get_count_model_number(test_number, model_number)
            my_answer = self.test_solve.get_count_model_number(test_number, model_number)
            self.assertTrue(right_answer == my_answer,
                             "[-] 第 {} 个能被 {} 整除的正整数应该是 {}".format(test_number, model_number, right_answer))

    def test_get_count_models_number(self):
        """
        给定数 a, b, c, 表示要求第 a 个能被 b 或 c 整除的数
        """
        for i in range(10 ** 2):
            test_data = random.randint(1, 10 ** 3), random.randint(2, 55), random.randint(2, 55)
            right_answer = self.get_count_models_number(*test_data)
            my_answer = self.test_solve.get_count_models_number(*test_data)

            a, b, c = test_data
            self.assertTrue(right_answer == my_answer,
                             "[-] 第 {} 个能被 {} 或 {} 整除的正整数应该是 {}".format(a, b, c, right_answer))

    def test_solve(self):
        test_data = 2333, 2, 3
        right_answer = self.get_count_models_number(*test_data)
        my_answer = self.test_solve.solve()
        self.assertTrue(right_answer == my_answer, "[-] 答案 {} 不对, 不信提交试试".format(my_answer))

    def get_count_models_number(self, count, *model_numbers):
        """
        求解第 count 个能整除 model_numbers 中的数字
        :param count: int(), 要求第几个?
        :param model_numbers: list(), 比如 [2, 3], 表示求的答案要么被 2 整除, 要么被 3 整除
        :return: int(), 第 count 个符合条件的数字
        """
        i = 0
        for number in self.return_infinite_number():
            for each_model_number in model_numbers:
                if self.is_module(number, each_model_number):
                    i += 1
                    break

            if i >= count:
                return number

    def get_count_model_number(self, count, model_number):
        i = 0
        for number in self.return_infinite_number():
            if self.is_module(number, model_number):
                i += 1

            if i >= count:
                return number

    @staticmethod
    def is_module(number, module):
        """
        判断一个数是否能被另外一个数整除
        :param number: int(), 待判断的数, 比如 33
        :param module: int(), 除数, 比如 3
        :return: Boolean(), 比如 33 % 3 == 0, 所以返回 True
        """
        return number % module == 0

    @staticmethod
    def return_infinite_number():
        """
        返回 2, 3, 4 ,5 ,6, ... 无穷大
        :return:
        """
        number = 1
        while True:
            number += 1
            yield number


if __name__ == "__main__":
    pass
