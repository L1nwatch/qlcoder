#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.13 题 10
    1. 计算平均值以及前移大于平均值的数
    2. 首字母大写转换
    3. 计算周边元素平均值
"""
import unittest
import io
import random
import sys

from solve10 import Solve
from contextlib import redirect_stdout

__author__ = '__L1n__w@tch'


class TestSolve(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.test_solve = Solve()

    def test_count_average_and_move_big(self):
        test_data = [46, 30, 32, 40, 6, 17, 45, 15, 48, 26]

        # 检查打印值, 打印值为平均值
        with io.StringIO() as buf, redirect_stdout(buf):
            self.test_solve.count_average_and_move_big(test_data)
            my_answer = buf.getvalue()
        right_answer = "30.5\n"
        self.assertEqual(right_answer, my_answer)

        # 检查返回值, 返回值为移动后的输出
        right_answer = [46, 32, 40, 45, 48, 30, 6, 17, 15, 26]
        my_answer = self.test_solve.count_average_and_move_big(test_data)
        self.assertEqual(right_answer, my_answer)

        for i in range(10 ** 2):
            test_data = list()
            for j in range(10 ** 2):
                test_data.append(random.randint(0, 10 ** 4))

            right_print, right_return = self.count_average_and_move_big(test_data)

            # 检查打印值
            with io.StringIO() as buf, redirect_stdout(buf):
                self.test_solve.count_average_and_move_big(test_data)
                my_answer = buf.getvalue()
            self.assertEqual(right_print, my_answer)

            # 检查返回值
            my_answer = self.test_solve.count_average_and_move_big(test_data)
            self.assertEqual(right_return, my_answer)

    def test_str_title(self):
        old_standard_in = sys.stdin

        test_data = io.StringIO("I am a student to take the examination")
        right_answer = 'I Am A Student To Take The Examination'
        sys.stdin = test_data
        my_answer = self.test_solve.str_title()
        self.assertEqual(right_answer, my_answer)

        sys.stdin = old_standard_in

        with open("usernames.txt", "r") as f:
            words = f.readlines()

        for i in range(10 ** 4):
            test_data = str()
            for j in range(random.randint(1, 2 ** 8) + 1):
                test_data += random.choice(words).strip() + " "
            test_data = test_data.rstrip(" ")
            right_answer = test_data.title()

            # input
            test_data = io.StringIO(test_data)
            sys.stdin = test_data
            my_answer = self.test_solve.str_title()
            sys.stdin = old_standard_in

            # assert
            self.assertEqual(my_answer, right_answer)

    def test_count_margin_average(self):
        test_list = [[0, 1, 2, 7, 9], [1, 9, 7, 4, 5], [2, 3, 8, 3, 1], [4, 5, 6, 8, 2], [5, 9, 1, 4, 1]]
        right_answer = 3.375
        my_answer = self.test_solve.count_margin_average(test_list)
        self.assertEqual(right_answer, my_answer)

        for i in range(10 ** 2):
            test_data = self.create_random_matrix()
            right_answer = self.count_margin_average(test_data)
            my_answer = self.test_solve.count_margin_average(test_data)
            self.assertEqual(right_answer, my_answer)

    @staticmethod
    def create_random_matrix():
        n = 3
        result_list = list()
        for i in range(n):
            temp_list = list()
            for j in range(n):
                temp_list.append(random.randint(1, 10 ** 3))
            result_list.append(temp_list)

        return result_list

    @staticmethod
    def count_average_and_move_big(test_list):
        average = sum(test_list) / len(test_list)
        big_list, small_list = list(), list()

        for each in test_list:
            if each > average:
                big_list.append(each)
            else:
                small_list.append(each)

        return "{}\n".format(average), big_list + small_list

    @staticmethod
    def count_margin_average(test_list):
        length = len(test_list)
        result_list = list()

        for i in range(length):
            for j in range(length):
                # 第一行元素, 或最后一行元素
                if i == 0 or i == length - 1:
                    result_list.append(test_list[i][j])
                # 第一列元素, 或最后一列元素
                elif j == 0 or j == length - 1:
                    result_list.append(test_list[i][j])

        return sum(result_list) / len(result_list)


if __name__ == "__main__":
    pass
