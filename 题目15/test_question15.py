#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.18 题 15
    1. 进制数转换
    2. 找出最长字符串
    3. 判断幻方
    4. 计算公式
"""
import unittest
import random
import string

from solve15 import Solve

__author__ = '__L1n__w@tch'


class TestSolve(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.test_solve = Solve()

    def test_number_convert(self):
        test_data = 8, 2
        right_answer = "1000"
        my_answer = self.test_solve.number_convert(*test_data)
        self.assertEqual(right_answer, my_answer)

        for i in range(10 ** 2):
            test_data = random.randint(1, 10 ** 5), random.randint(2, 9)
            right_answer = self.number_convert(*test_data)
            my_answer = self.test_solve.number_convert(*test_data)
            self.assertEqual(right_answer, my_answer)

    def test_find_longest_str(self):
        test_data = ["1", "22", "333", "1", "22", "4444", "1"]
        right_answer = "4444"
        my_answer = self.test_solve.find_longest_str(test_data)
        self.assertEqual(right_answer, my_answer)

        for i in range(10):
            test_data = ["".join(
                [random.choice(string.ascii_letters) for y in range(random.randint(1, 2 ** 8))]
            ) for x in range(random.randint(1, 10 ** 2))]
            right_answer = max(test_data, key=lambda x: len(x))
            my_answer = self.test_solve.find_longest_str(test_data)
            self.assertEqual(right_answer, my_answer)

    def test_is_magic_square_odd(self):
        test_data = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
        right_answer = True
        my_answer = self.test_solve.is_magic_square_odd(test_data)
        self.assertEqual(right_answer, my_answer)

        for i in range(10):
            right_answer = random.choice([True, False])
            test_data = self.create_odd_matrix(right_answer)
            my_answer = self.test_solve.is_magic_square_odd(test_data)
            right_answer = self.is_magic_square_odd(test_data)
            self.assertEqual(right_answer, my_answer)

    def test_compute_formula(self):
        test_data = 5
        right_answer = -10
        my_answer = self.test_solve.compute_formula(test_data)
        self.assertEqual(right_answer, my_answer)

        for i in range(10 ** 2):
            test_data = random.randint(2, 10 ** 3)
            right_answer = sum([2] + [-x for x in range(3, test_data + 1)])
            my_answer = self.test_solve.compute_formula(test_data)
            self.assertEqual(right_answer, my_answer)

    @staticmethod
    def magic_square_odd_generate(n):
        """
        参考 http://www.hsyyf.me/2012/04/22/%E5%B9%BB%E6%96%B9%E6%9E%84%E9%80%A0%EF%BC%88%E4%B8%80%EF%BC%89/
        :param n: 奇数 n
        :return: list(), 幻方矩阵
        """
        magic = [([0] * n) for i in range(n)]

        i = 0
        j = (n - 1) // 2
        magic[i][j] = 1
        for m in range(2, n * n + 1, 1):
            i0 = i
            j0 = j
            i = (i + n - 1) % n
            j = (j + n + 1) % n
            if magic[i][j] != 0:
                i = (i0 + n + 1) % n
                j = j0
            if i0 == 0 and j0 == n - 1:
                i = 1
                j = n - 1
            magic[i][j] = m

        return magic

    @staticmethod
    def is_magic_square_odd(a_list):
        length = len(a_list)

        # 判断行值是否相等
        answer = sum(a_list[0])
        for row in a_list:
            if answer != sum(row):
                return False

        # 判断列值是否相等
        for column in range(length):
            if answer != sum([x[column] for x in a_list]):
                return False

        # 判断主对角线
        result = 0
        for i in range(length):
            result += a_list[i][i]
        if answer != result:
            return False

        # 判断反对角线
        result = 0
        for i in range(length):
            result += a_list[i][length - i - 1]
        if answer != result:
            return False

        return True

    def create_odd_matrix(self, need_magic_square_odd):
        # 选取奇数出来
        n = 0
        while n % 2 == 0:
            n = random.randint(1, 10)

        if need_magic_square_odd:
            return self.magic_square_odd_generate(n)
        else:
            return self.create_random_matrix(n)

    @staticmethod
    def create_random_matrix(n):
        result_list = list()
        for i in range(n):
            temp_list = list()
            for j in range(n):
                temp_list.append(random.randint(1, 10 ** 3))
            result_list.append(temp_list)

        return result_list

    @staticmethod
    def number_convert(number, base):
        # 用标准库检验过了
        result = str()
        while True:
            result += str(number % base)
            if number // base == 0:
                break
            number //= base

        return "".join(reversed(result))


if __name__ == "__main__":
    pass
