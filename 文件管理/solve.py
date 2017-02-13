#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.13 遍历文件还好说, 关键是判断文件大小呢
"""
import os

__author__ = '__L1n__w@tch'


def solve():
    result_dict = dict()

    for root, dirs, files in os.walk("root"):
        for each_file in files:
            if each_file.endswith(".txt"):
                file_path = os.path.join(root, each_file)
                size = os.path.getsize(file_path)
                result_dict[file_path] = size

    max_size_file_path = max(result_dict.items(), key=lambda item: item[1])[0]

    with open(max_size_file_path, "r", encoding="gbk") as f:
        data = f.read()
    print(data)


if __name__ == "__main__":
    solve()
