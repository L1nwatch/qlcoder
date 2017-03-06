#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.03.06 讨论区也没什么好的资料可以参考, 但是提到了 munkres 匈牙利算法, 于是试一下, 好吧还真过了
"""
import munkres
import gmpy2

__author__ = '__L1n__w@tch'


def test_solve():
    """
    测试一下 munkres 库如何使用
    """
    matrix = [[39.4, 78.5, 81.0],
              [50.2, 68.0, 46.1]]
    m = munkres.Munkres()
    indexes = m.compute(matrix)
    print(indexes)


def get_matrix_from_data_file():
    matrix = list()

    # 读取所有乘客的坐标
    with open("passenger.txt", "r") as f:
        passengers = [x.rstrip() for x in f.readlines()]

    # 读取所有司机的坐标
    with open("ubercar.txt", "r") as f:
        cars = [x.rstrip() for x in f.readlines()]

    # 计算并存在矩阵中
    for each_passenger in passengers:
        x1, y1 = each_passenger.split(" ")
        x1, y1 = gmpy2.mpz(float(x1)), gmpy2.mpz(float(y1))
        cost_line = list()
        for each_car in cars:
            x2, y2 = each_car.split(" ")
            x2, y2 = float(x2), float(y2)
            cost = gmpy2.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
            cost_line.append(cost)
        matrix.append(cost_line)

    return matrix


def solve():
    matrix = get_matrix_from_data_file()
    m = munkres.Munkres()
    indexes = m.compute(matrix)
    for row, column in indexes:
        print("P{}-U{}".format(row + 1, column + 1))


if __name__ == "__main__":
    solve()
