#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.20 题 17
    1. 字符串交叉拼接
    2. 删除字符串指定字符
    3. 矩阵行交换
"""
import unittest
import random
import string
import copy

from solve17 import Solve

__author__ = '__L1n__w@tch'


class TestSolve(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.test_solve = Solve()

    def test_str_cross_combine(self):
        test_data = "abcdefg", "1234"
        right_answer = "a4b3c2d1efg"
        my_answer = self.test_solve.str_cross_combine(*test_data)
        self.assertEqual(right_answer, my_answer)

        test_data = "1234", "abcdefg"
        right_answer = "1g2f3e4dcba"
        my_answer = self.test_solve.str_cross_combine(*test_data)
        self.assertEqual(right_answer, my_answer)

        str_set = string.ascii_letters + string.digits
        for i in range(10 ** 2):
            test_data = "".join([random.choice(str_set) for x in range(random.randint(1, 10 ** 2))]), \
                        "".join([random.choice(str_set) for x in range(random.randint(1, 10 ** 2))])
            right_answer = self.str_cross_combine(*test_data)
            my_answer = self.test_solve.str_cross_combine(*test_data)
            self.assertEqual(right_answer, my_answer)

    def test_str_delete_odd_ascii(self):
        test_data = "ABCDEFG12345"
        right_answer = "BDF12345"
        my_answer = self.test_solve.str_delete_odd_ascii(test_data)
        self.assertEqual(right_answer, my_answer)

        for i in range(10 ** 2):
            test_str = [random.choice(string.ascii_letters + string.digits) for x in range(random.randint(1, 10 ** 2))]
            right_answer = self.str_delete_odd_ascii(test_str)
            my_answer = self.test_solve.str_delete_odd_ascii(test_str)
            self.assertEqual(right_answer, my_answer)

    def test_exchange_matrix_row(self):
        test_data = 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        right_answer = [[7, 8, 9], [4, 5, 6], [1, 2, 3], [10, 11, 12]]
        my_answer = self.test_solve.exchange_matrix_row(*test_data)
        self.assertEqual(right_answer, my_answer)

        for i in range(10 ** 2):
            test_matrix = self.create_random_matrix()
            test_data = random.randint(1, len(test_matrix)), copy.deepcopy(test_matrix)
            right_answer = self.exchange_matrix_row(*test_data)
            my_answer = self.test_solve.exchange_matrix_row(*test_data)
            self.assertEqual(right_answer, my_answer)

    @staticmethod
    def str_cross_combine(a, b):
        list_a = list(a)
        answer = str()
        reversed_b = list(reversed(b))

        while len(list_a) > 0 or len(reversed_b) > 0:
            if len(list_a) > 0:
                answer += list_a.pop(0)
            if len(reversed_b) > 0:
                answer += reversed_b.pop(0)

        return answer

    @staticmethod
    def str_delete_odd_ascii(a_str):
        result = str()
        for i, each_char in enumerate(a_str):
            if i % 2 != 0 or ord(each_char) % 2 == 0:
                result += each_char
        return result

    @staticmethod
    def create_random_matrix():
        n = random.randint(1, 10)
        m = random.randint(1, 10)

        result_list = list()
        for i in range(n):
            temp_list = list()
            for j in range(m):
                temp_list.append(random.randint(1, 10 ** 2))
            result_list.append(temp_list)

        return result_list

    @staticmethod
    def exchange_matrix_row(k, matrix):
        matrix[k - 1], matrix[0] = matrix[0], matrix[k - 1]
        return matrix


if __name__ == "__main__":
    pass
