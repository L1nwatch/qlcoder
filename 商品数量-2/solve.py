#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.12 这道题还真挺棘手的
"""
import gmpy2

__author__ = '__L1n__w@tch'


def parse_line(raw_data):
    """
    解析每一行
    :param raw_data: str(), 比如 "up 17 913"
    :return: tuple, ("up", 17, 913)
    """
    operation, number, money = raw_data.split(" ")
    return operation, int(number), int(money)


def solve():
    clothes_dict = dict()  # 保存衣服数量
    # 初始化
    for i in range(10 ** 6):
        clothes_dict.setdefault(i, gmpy2.mpz(0))

    final_answer = int()

    with open("144043063958496.txt", "r") as f:
        for each_line in f:
            operation, num1, num2 = parse_line(each_line)
            if operation == "up":
                clothes_dict[num2] += num1
            elif operation == "down":
                clothes_dict[num2] -= num1
            elif operation == "query":
                query_result = int()
                for i in range(num1, num2 + 1):
                    query_result += clothes_dict[i]
                final_answer += query_result

    print("最终答案: {}".format(final_answer))


if __name__ == "__main__":
    solve()
