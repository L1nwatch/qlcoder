#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 无边界地图

参考讨论区给出的算法进行实现
题目链接: http://www.qlcoder.com/task/75d8
"""

__author__ = '__L1n__w@tch'


class Point:
    def __init__(self, x=None, y=None, is_alive=False):
        # is_alive 为 True 表示是生命体
        self.x, self.y, self.is_alive = x, y, is_alive

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return "({}, {}) - {}".format(self.x, self.y, "生命体" if self.is_alive else "空地")


def update_count_dict(alive_list):
    """
    遍历列表，对所有生命体，将其周围8个格子的"生命体计数"加一。
    :param alive_list: 生命体列表
    :return: None, 将结果直接更新到 count_dict 中
    """
    count_dict = dict()

    for each_point in alive_list:
        # 依次更新 <左上, 上, 右上, 左, 右, 左下, 下, 右下> 共 8 个各自的数据
        point_west_north = Point(each_point.x - 1, each_point.y + 1)
        point_west_north.is_alive = True if point_west_north in alive_list else False
        count_dict[point_west_north] = count_dict.get(point_west_north, 0) + 1

        point_north = Point(each_point.x, each_point.y + 1)
        point_north.is_alive = True if point_north in alive_list else False
        count_dict[point_north] = count_dict.get(point_north, 0) + 1

        point_north_east = Point(each_point.x + 1, each_point.y + 1)
        point_north_east.is_alive = True if point_north_east in alive_list else False
        count_dict[point_north_east] = count_dict.get(point_north_east, 0) + 1

        point_west = Point(each_point.x - 1, each_point.y)
        point_west.is_alive = True if point_west in alive_list else False
        count_dict[point_west] = count_dict.get(point_west, 0) + 1

        point_east = Point(each_point.x + 1, each_point.y)
        point_east.is_alive = True if point_east in alive_list else False
        count_dict[point_east] = count_dict.get(point_east, 0) + 1

        point_west_south = Point(each_point.x - 1, each_point.y - 1)
        point_west_south.is_alive = True if point_west_south in alive_list else False
        count_dict[point_west_south] = count_dict.get(point_west_south, 0) + 1

        point_south = Point(each_point.x, each_point.y - 1)
        point_south.is_alive = True if point_south in alive_list else False
        count_dict[point_south] = count_dict.get(point_south, 0) + 1

        point_west = Point(each_point.x + 1, each_point.y - 1)
        point_west.is_alive = True if point_west in alive_list else False
        count_dict[point_west] = count_dict.get(point_west, 0) + 1

    return count_dict


def update_alive_list(count_dict, alive_list):
    """
    遍历字典，对周围有生命体的格子，检查它是否能继续生存/繁殖出新的生命体。将结果存储到新列表中
    :param count_dict: 计数器字典
    :param alive_list: 生命体列表
    :return: list(), 更新后的结果
    """
    result_list = list()

    for each_point, count in count_dict.items():
        # 空地周围有 3 个生命体
        if not each_point.is_alive and count == 3:
            each_point.is_alive = True
            result_list.append(each_point)
        # 生命体周围有 2 或 3 个生命体
        elif each_point.is_alive and 2 <= count <= 3:
            each_point.is_alive = True
            result_list.append(each_point)
        else:
            each_point.is_alive = False

    return result_list


def init():
    """
    初始化游戏开始的情况, 即有 5 个生命体的情况
    :return: tuple(), (list, dict), 分别表示含有生命体的列表, 以及一个计数器字典
    """
    alive_list = list()
    count_dict = dict()

    # 默认最中间那个作为 0,0
    alive_list.append(Point(0, 0, True))
    alive_list.append(Point(0, 1, True))
    alive_list.append(Point(0, -1, True))
    alive_list.append(Point(-1, 0, True))
    alive_list.append(Point(1, 1, True))

    return alive_list, count_dict


def solve():
    # 初始化游戏开始的情况, 即有 5 个生命体的情况
    alive_list, count_dict = init()
    result_dict = dict()
    times = 0

    while times < 2000:
        # 遍历列表，对所有生命体，将其周围8个格子的"生命体计数"加一。
        count_dict = update_count_dict(alive_list)

        # 遍历字典，对周围有生命体的格子，检查它是否能继续生存/繁殖出新的生命体。将结果存储到新列表中
        alive_list = update_alive_list(count_dict, alive_list)

        # 打印列表长度
        times += 1
        # print("[*] 第 {times} 轮迭代后: {0}".format(alive_list, times=times))
        # print("[*] 第 {times} 轮迭代后: {times}-{0}".format(len(alive_list), times=times))
        result_dict[times] = len(alive_list)

    max_result = max(result_dict.items(), key=lambda item: item[1])
    print("[*] 第 {times} 迭代得到的值最大, 为: {count}, 即 {times}-{count}".format(times=max_result[0],
                                                                         count=max_result[1]))


if __name__ == "__main__":
    solve()
