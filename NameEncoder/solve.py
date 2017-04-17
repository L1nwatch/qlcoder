#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 编码文件名的问题

话说自己没啥思路, 估计是得看讨论区了- -

题目链接: http://www.qlcoder.com/task/76b9
"""
import unittest

__author__ = '__L1n__w@tch'


class TestAnswer(unittest.TestCase):
    def test_encode(self):
        pass

    def test_decode(self):
        pass

    def test_answer(self):
        raw_list = ["0", "1", "10", "11", "100"]
        my_answer = [encode(int(x)) for x in raw_list]
        my_answer = sorted(my_answer, key=lambda x: decode(x))
        for right_answer, mine in zip(raw_list, my_answer):
            self.assertEqual(int(right_answer), int(mine[2:]), "[-] Raw: {}, Mine: {}".format(raw_list, my_answer))

    def test_rate(self):
        raw_list = ["1", "12345679", "12345680", "123456789", "123456790", "123456791", "123456792", "1234567890"]
        my_answer = [encode(int(x)) for x in raw_list]

        raw_length = sum(len(x) for x in raw_list)
        my_length = sum(len(x) for x in my_answer)
        rate = my_length / raw_length
        self.assertTrue(rate < 1.3, "[-] Rate: {}".format(rate))


def encode(n):
    return "{}{}".format(str(len(str(n))).zfill(2), n)


def decode(s):
    return int(s[2:])


if __name__ == "__main__":
    pass
