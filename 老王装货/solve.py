#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.19 解决一下动态规划的问题
参考资料:
    http://www.cnblogs.com/SDJL/archive/2008/08/22/1274312.html
    还是讲得不错的
"""

__author__ = '__L1n__w@tch'

mark = [[0 for j in range(5000)] for i in range(14)]
test_data = {
    1: 509, 2: 838, 3: 924, 4: 650,
    5: 604, 6: 793, 7: 564, 8: 651,
    9: 697, 10: 649, 11: 747, 12: 787,
    13: 701, 14: 605, 15: 644,
}


def recursion_make(i, remain, order):
    """
    递归解决
    :param i: int(), 表示第几个货物
    :param remain: int(), 表示还剩下多少重量可以放
    :param order: str(), 表示之前存放货物的编号
    :return: tuple, (int(), str()), 分别表示前 i 个货物最重是多少, 以及前 i 个货物的编号
    """
    global mark, test_data
    result = 0
    new_order = str()

    # 还有货物
    if i > 0:
        # 如果装进去
        plan_a_result, plan_a_order = 0, order
        if remain >= test_data[i]:
            plan_a_result, plan_a_order = recursion_make(i - 1, remain - test_data[i], order)
            plan_a_result += test_data[i]

        # 如果不装进去
        plan_b_result, plan_b_order = recursion_make(i - 1, remain, order)

        if plan_a_result > plan_b_result:
            if plan_a_order != "":
                new_order = "{}-{}".format(plan_a_order, i)
            else:
                new_order = "{}".format(i)
        else:
            new_order = plan_b_order

        result = max(plan_a_result, plan_b_result)

    return result, new_order


def solve():
    global test_data
    max_result, order = recursion_make(len(test_data), 5000, "")
    print(max_result)
    print(order)


if __name__ == "__main__":
    solve()
