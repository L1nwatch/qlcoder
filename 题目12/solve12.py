#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.15 题 12
    1. 字符串面值的整数求和
    2. 统计大小写字母格式
    3. 保留小数位数
"""
__author__ = '__L1n__w@tch'


class Solve:
    @staticmethod
    def compute_int_add(str1, str2):
        """
        将字符串分别转换成面值相同的整数, 并执行加法操作, 且将结果作为函数返回值返回
        :param str1: str(), 比如 "32486"
        :param str2: str(), 比如 "12345"
        :return: int(), 比如 44831
        """
        pass

    @staticmethod
    def count_upper_and_lower(a_str):
        """
        给定一个字符串, 分别统计大写字母和小写字母的个数, 最终打印格式比如: upper=6,lower=8
        :param a_str: str(), 比如 "AAaaBBbb123CCcccd"
        :return: None; 直接按照格式要求进行打印即可
        """
        pass

    @staticmethod
    def save_two_decimal_places(a_float_number):
        """
        将变量的值保留两位小数, 即要求对第三位进行四舍五入(规定给定的值为整数)
        比如给定 1234.567 (不一定只给 3 位小数), 要求对第三位四舍五入, 保留两位小数, 于是答案就是 1234.57
        :param a_float_number: float(), 比如 1234.567
        :return: str(), 保留两位小数之后的结果, 比如 "1234.57"
        """
        pass


if __name__ == "__main__":
    pass
