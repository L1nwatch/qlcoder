#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.14 题 11
    1. 计算平均值以及前移小于平均值的数
    2. 统计元音字母个数
    3. 计算周边元素之和
"""
__author__ = '__L1n__w@tch'


class Solve:
    @staticmethod
    def count_average_and_pre_move_small(test_list):
        """
        给定一个列表
        任务一:
            计算平均值, 将平均值打印出来, 比如算出来的平均值为 30.5, 则打印出 30.5, 用字符串表示打印结果即为: "30.5\n"
        任务二:
            将小于平均值的数, 按照列表原来的顺序依次摆放到列表的前面;
            将大于等于平均值的数, 按照列表原来的顺序依次摆放的列表的后面
        具体例子:
            [46, 30, 32, 40, 6, 17, 45, 15, 48, 26]
            (1) 计算平均值, 得到 30.5
            (2) 依次观察每个元素, 大于平均值的数依次为: [46, 32, 40, 45, 48], 小于等于的依次为: [30, 6, 17, 15, 26]
                于是最终答案为: [30, 6, 17, 15, 26, 46, 32, 40, 45, 48]
        :param test_list: list(), 比如 [46, 30, 32, 40, 6, 17, 45, 15, 48, 26]
        :return: list(), 根据平均值移动数据后的列表, 比如 [30, 6, 17, 15, 26, 46, 32, 40, 45, 48] ; 平均值直接打印即可
        """
        average = sum(test_list) / len(test_list)
        big_list, small_list = list(), list()

        for each in test_list:
            if each < average:
                big_list.append(each)
            else:
                small_list.append(each)

        print(average)
        return big_list + small_list

    @staticmethod
    def count_vocal():
        """
        从标准输入流读入一行英文文本, 每个英文单词以空格隔开, 比如
            "I am a student to take the examination"
        要求将其中每个单词的第一个字母改成大写, 然后返回此文本行, 比如
            "I Am A Student To Take The Examination"
        :return: str(), 转换首字母大写后的字符串, 比如 'I Am A Student To Take The Examination'
        """
        test_data = input("")
        answer = list()
        for each in ["a", "e", "i", "o", "u"]:
            answer.append(str(test_data.lower().count(each)))
        return " ".join(answer).rstrip(" ")

    @staticmethod
    def count_margin_sum(test_list):
        """
        给定一个 n*m 的矩阵, 此处不固定, 给例子为 n, m 均为 5 的情况:
            [
                [0, 1, 2, 7, 9],
                [1, 9, 7, 4, 5],
                [2, 3, 8, 3, 1],
                [4, 5, 6, 8, 2],
                [5, 9, 1, 4, 1]
            ]
        要求计算矩阵周边元素的和, 并将和作为打印值打印出来, 打印结果不带换行符
        如示例中, 周边元素即为 上: [0, 1, 2, 7, 9], 左: [1, 2, 4, 5], 右: [5, 1, 2, 1], 下: [9, 1, 4]
        :param test_list: list(), 矩阵, 此处不固定维数, 比如 4*5 的话:
            [[1, 3, 5, 7, 9], [2, 9, 9, 9, 4], [6, 9, 9, 9, 8], [1, 3, 5, 7, 0]]
        :return: int(), 计算得到的和, 比如 61
        """
        row = len(test_list)
        column = len(test_list[0])
        result_list = list()

        for i in range(row):
            for j in range(column):
                # 第一行元素, 或最后一行元素
                if i == 0 or i == row - 1:
                    result_list.append(test_list[i][j])
                # 第一列元素, 或最后一列元素
                elif j == 0 or j == column - 1:
                    result_list.append(test_list[i][j])

        return sum(result_list)


if __name__ == "__main__":
    pass
