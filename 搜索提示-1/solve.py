#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 学习一下中文转拼音的东西

参考讨论区, 试着用一下 pypinyin, 准确率只有 590+
"""
import pypinyin

__author__ = '__L1n__w@tch'


def solve():
    result = list()
    result_to_file = list()

    with open("145630854135681.txt", "r") as f:
        for each_line in f:
            each_line = each_line.strip()
            parse_result = pypinyin.lazy_pinyin(each_line)
            result.append("".join(parse_result))
            result_to_file.append("{} -> {}".format(each_line, "-".join(parse_result)))

    with open("pinyin_result_python.txt", "w") as f:
        for each_line in result_to_file:
            f.write("{}\n".format(each_line))

    print("[*] 答案要求的结果为: {}".format("-".join(result)))


if __name__ == "__main__":
    solve()
